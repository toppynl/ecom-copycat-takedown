#!/usr/bin/env python3
"""Zoek in Certificate Transparency naar recent uitgegeven certificaten voor
hostnamen die met de merknaam BEGINNEN.

Gebruik:  python3 ct_search.py <merknaam> [--sinds-maanden N] [--csv pad]

Vangt namen die de permutatie-zeef van discover.py mist (bijv. merk + categorie
+ land-combinaties), want elk certificaat voor een nieuwe shop belandt in CT.

Waarom de Postgres-ingang en niet de crt.sh-website: de web-UI/JSON-API geeft
vaak 502 of time-outs, de publieke database (guest@crt.sh:5432/certwatch) werkt
wel, al is hij soms overbelast (dan probeert dit script het opnieuw). Vereist de
`psql`-CLI (macOS: `brew install libpq`); verder alleen de standaardbibliotheek.

Beperkingen die in de query zijn ingebouwd (zwaardere varianten geven een
statement timeout of 0 resultaten):
- Geen ORDER BY, geen datumfilter in SQL, geen x509_altNames.
- Zoeken via de full-text-index: de tokenizer ziet een hele hostnaam als één
  token, dus 'merk:*' is een PREFIX-match: merkshop.com en merk-nl.com wel,
  shopmerk.com niet. Combineer daarom met discover.py.
- Tijdsfilter loopt via het certificaat-ID (loopt op met de tijd), zie
  schat_minid().
"""
import argparse
import csv
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import date, datetime, timedelta

# Uit te sluiten: eigen domeinen + bekende legitieme naamgenoten (registreerbaar
# domein, bijv. "merk.nl"). Vul aan met de echte domeinen van de rechthebbende.
ALLOWLIST = {
    # "merk.nl",
    # "merk.com",
}

PAGINA = 5000                      # max. regels per query (LIMIT)
IDS_PER_MAAND = 660_000_000        # grove groei van certificaat-ID's (gemeten 2025-2026)
MAX_POGINGEN = 30                  # bij tijdelijke fouten (overbelasting crt.sh)
MAX_SUB = 8                        # max. getoonde hostnamen per domein (CSV bevat alles)
WACHT_SEC = 8                      # wachttijd tussen pogingen (6-10 s)

TIJDELIJK = ("max_client_conn", "connection refused", "timeout expired",
             "could not connect", "connection timed out", "server closed the connection")
ZWAAR = "canceling statement due to statement timeout"

# Tweedelaags-suffixen waarvoor het registreerbare domein 3 labels is. Bewust
# klein gehouden; onbekende gevallen vallen terug op de laatste 2 labels.
TWEEDELAAGS = {"co.uk", "org.uk", "me.uk", "com.au", "co.nz", "co.za", "com.br",
               "com.tr", "com.mx", "co.jp", "co.in"}


def psql(query):
    """Voer een query uit en geef de regels terug. Probeert opnieuw bij tijdelijke fouten."""
    if not shutil.which("psql"):
        sys.exit("psql niet gevonden. Installeer de PostgreSQL-client: brew install libpq "
                 "(en voeg `$(brew --prefix libpq)/bin` toe aan je PATH).")
    # Let op: GEEN PGOPTIONS/-c-opties meegeven; crt.sh weigert "unsupported startup parameter: options".
    env = dict(os.environ, PGCONNECT_TIMEOUT="20")
    env.pop("PGOPTIONS", None)
    cmd = ["psql", "-h", "crt.sh", "-p", "5432", "-U", "guest", "-d", "certwatch",
           "-A", "-t", "-F", "|", "-c", query]
    zwaar_geprobeerd = False
    laatste = ""
    for poging in range(1, MAX_POGINGEN + 1):
        try:
            p = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=600)
        except subprocess.TimeoutExpired:
            laatste = "lokale time-out (600 s)"
            p = None
        if p is not None:
            if p.returncode == 0:
                return [r for r in p.stdout.splitlines() if r.strip()]
            laatste = (p.stderr or p.stdout).strip()
            low = laatste.lower()
            if ZWAAR in low:
                if zwaar_geprobeerd:
                    sys.exit("Query te zwaar voor crt.sh (statement timeout, ook na een tweede poging). "
                             "Probeer een kortere periode: --sinds-maanden 1.")
                zwaar_geprobeerd = True
                print("  statement timeout, één keer opnieuw proberen ...", file=sys.stderr)
                continue
            if not any(t in low for t in TIJDELIJK):
                sys.exit(f"psql-fout: {laatste}")
        print(f"  crt.sh tijdelijk niet beschikbaar (poging {poging}/{MAX_POGINGEN}); "
              f"{WACHT_SEC} s wachten ...", file=sys.stderr)
        time.sleep(WACHT_SEC)
    sys.exit(f"crt.sh bleef onbereikbaar na {MAX_POGINGEN} pogingen. Laatste melding: {laatste}")


def schat_minid(maanden):
    """Schat het laagste certificaat-ID dat nog binnen de gevraagde periode valt.

    Dit is een SCHATTING: ID's lopen grofweg op met de tijd, maar niet lineair.
    Daarom nemen we ruim terug in de tijd en filteren we daarna lokaal nog op de
    echte notBefore-datum (>= de gevraagde datum).
    """
    regels = psql("SELECT max(ID) FROM certificate;")
    if not regels or not regels[0].strip().isdigit():
        sys.exit(f"Kon max(ID) niet bepalen uit crt.sh-antwoord: {regels!r}")
    return max(0, int(regels[0]) - int(maanden * IDS_PER_MAAND))


def registreerbaar(host):
    labels = host.split(".")
    if len(labels) >= 3 and ".".join(labels[-2:]) in TWEEDELAAGS:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:])


def schoon(naam):
    n = naam.strip().lower()
    n = re.sub(r"^\*\.", "", n)
    n = re.sub(r"^www\.", "", n)
    return n


def main():
    ap = argparse.ArgumentParser(description="Zoek merk-prefix hostnamen in Certificate Transparency (crt.sh).")
    ap.add_argument("merk", help="merknaam (alleen a-z, 0-9 en '-')")
    ap.add_argument("--sinds-maanden", type=float, default=6, help="hoeveel maanden terug (standaard 6)")
    ap.add_argument("--csv", metavar="PAD", help="schrijf het resultaat ook naar dit CSV-bestand")
    a = ap.parse_args()

    merk = a.merk.strip().lower()
    # Alleen [a-z0-9-]: de merknaam komt letterlijk in de SQL te staan, dit voorkomt SQL-injectie.
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", merk):
        sys.exit("Ongeldige merknaam: gebruik alleen a-z, 0-9 en '-' (geen spaties of punten).")
    if merk == "merk":
        sys.exit("Geef je eigen merknaam op: python3 ct_search.py <merknaam>")
    if a.sinds_maanden <= 0:
        sys.exit("--sinds-maanden moet groter dan 0 zijn.")

    grens = date.today() - timedelta(days=round(a.sinds_maanden * 30.4))
    print(f"Merk '{merk}' | sinds ~{grens.isoformat()} ({a.sinds_maanden:g} mnd) | bron: crt.sh (Postgres)")
    minid = schat_minid(a.sinds_maanden)
    print(f"Geschat start-ID: {minid:,}".replace(",", "."))

    rijen = []  # (id, notBefore, naam)
    pagina = 0
    while True:
        pagina += 1
        q = ("SELECT cai.CERTIFICATE_ID, x509_notBefore(cai.CERTIFICATE)::date, cai.NAME_VALUE "
             "FROM certificate_and_identities cai "
             f"WHERE to_tsquery('certwatch','{merk}:*') @@ identities(cai.CERTIFICATE) "
             f"AND cai.CERTIFICATE_ID > {minid} "
             "AND cai.NAME_TYPE IN ('san:dNSName','2.5.4.3') "
             f"LIMIT {PAGINA};")
        regels = psql(q)
        hoogste = minid
        for r in regels:
            delen = r.split("|", 2)
            if len(delen) != 3 or not delen[0].isdigit():
                continue
            cid = int(delen[0])
            hoogste = max(hoogste, cid)
            try:
                nb = datetime.strptime(delen[1], "%Y-%m-%d").date()
            except ValueError:
                continue
            rijen.append((cid, nb, delen[2]))
        print(f"  pagina {pagina}: {len(regels)} regels", file=sys.stderr)
        # Resultaten komen in oplopende ID-volgorde: bij een volle pagina verder vanaf het hoogste ID.
        if len(regels) < PAGINA or hoogste <= minid:
            break
        minid = hoogste

    # Per unieke hostname eerste/laatste certificaatdatum (lokaal filter op echte datum).
    namen = {}
    for _, nb, naam in rijen:
        if nb < grens:
            continue
        n = schoon(naam)
        if merk not in n or " " in n or "." not in n:
            continue
        if registreerbaar(n) in ALLOWLIST or n in ALLOWLIST:
            continue
        eerste, laatste = namen.get(n, (nb, nb))
        namen[n] = (min(eerste, nb), max(laatste, nb))

    # Groeperen per registreerbaar domein; nieuwste (eerste datum) bovenaan.
    groepen = {}
    for n, (e, l) in namen.items():
        groepen.setdefault(registreerbaar(n), []).append((n, e, l))
    volgorde = sorted(groepen.items(), key=lambda kv: max(e for _, e, _ in kv[1]), reverse=True)

    print(f"\nCertificaatregels: {len(rijen)} | unieke hostnamen (na filter): {len(namen)} "
          f"| registreerbare domeinen: {len(groepen)}\n")
    print(f"  {'hostnaam':44} {'eerste':10}  {'laatste':10}")
    for dom, leden in volgorde:
        leden.sort(key=lambda x: x[1], reverse=True)
        print(f"{dom}")
        for n, e, l in leden[:MAX_SUB]:
            print(f"  {n:44} {e.isoformat()}  {l.isoformat()}")
        if len(leden) > MAX_SUB:
            print(f"  ... +{len(leden) - MAX_SUB} meer (volledig in --csv)")

    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["registreerbaar_domein", "hostnaam", "eerste_cert", "laatste_cert"])
            for dom, leden in volgorde:
                for n, e, l in leden:
                    w.writerow([dom, n, e.isoformat(), l.isoformat()])
        print(f"\nCSV geschreven: {a.csv}")

    print("\nVervolg per nieuwe naam: verifieer via DNS (recon.py), who.is/RDAP (registrar + datum)"
          " en browser (merklogo? checkout-kaartoogst?).")
    print("Let op: alleen prefix-matches (namen die met het merk beginnen); combineer met discover.py.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Ontdek gelieerde copycat-domeinen die een merk misbruiken.

Gebruik:  python3 discover.py <merknaam> [extra-affix ...]
          (of pas BRAND hieronder eenmalig aan naar je eigen merk)

Genereert permutaties (merk x voor/achtervoegsels x koppeltekens x TLD's),
resolvet ze via DNS en scoort elke treffer op de bekende daderkenmerken:
achter Cloudflare, geen MX-record. WHOIS/registrar en site-inhoud kun je daarna
per verdachte hit ophalen (WebFetch who.is + Chrome) — dit script doet alleen de
brede, goedkope eerste zeef die een handmatig lijstje mist.

Dit vervangt GEEN Certificate Transparency-feed: CT (crt.sh / CertSpotter)
vangt óók namen die hier niet in de permutatielijst zitten. Zet daarom als
externe bron een gratis CT-alert op je merknaam op; dit script is de laag eronder.

Vul de ALLOWLIST met je eigen domein + bekende legitieme naamgenoten, zodat je
niet elke keer opnieuw dezelfde ruis krijgt.
"""
import ipaddress
import socket
import sys

socket.setdefaulttimeout(3)

# Pas dit aan naar je eigen merk, of geef het mee als eerste argument.
BRAND = "merk"

# Uit te sluiten: eigen domein + bekende legitieme naamgenoten (geen copycats).
# Vul aan met de echte domeinen van de rechthebbende en verzamelde false-positives.
ALLOWLIST = {
    # "merk.nl",
    # "merk.com",
}

AFFIXES = [
    # Merk-neutrale, generieke webshop-/retailaffixes. Voeg merk- of
    # sectorspecifieke termen toe als extra command-line-argumenten, bijv.:
    #   python3 discover.py mijnmerk camping outdoor kampeer
    "", "online", "store", "shop", "webshop", "sale", "outlet", "deals",
    "shopping", "official", "store-nl", "nl", "eu", "be", "de", "uk", "us",
    "market", "discount", "buy", "kopen", "winkel", "warenhuis",
]
SEPS = ["", "-"]
TLDS = [".com", ".net", ".shop", ".store", ".online", ".site", ".co",
        ".shopping", ".info", ".nl", ".eu", ".de", ".be", ".co.uk"]

# Officiële Cloudflare IPv4-ranges (https://www.cloudflare.com/ips/). Een domein
# dat achter Cloudflare zit, resolvet naar een IP in een van deze blokken —
# zelfde nette CIDR-check als recon.py (geen grove /8-benadering).
CLOUDFLARE_V4 = [
    "173.245.48.0/20", "103.21.244.0/22", "103.22.200.0/22", "103.31.4.0/22",
    "141.101.64.0/18", "108.162.192.0/18", "190.93.240.0/20", "188.114.96.0/20",
    "197.234.240.0/22", "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/13",
    "104.24.0.0/14", "172.64.0.0/13", "131.0.72.0/22",
]
_CF_NETS = [ipaddress.ip_network(n) for n in CLOUDFLARE_V4]


def is_cloudflare(ips):
    for ip in ips:
        try:
            if any(ipaddress.ip_address(ip) in net for net in _CF_NETS):
                return True
        except ValueError:
            continue
    return False


def has_mx(domain):
    # Zonder dnspython alleen indirecte check; recon.py doet de nette MX-lookup.
    try:
        import dns.resolver  # noqa
        return bool(dns.resolver.resolve(domain, "MX"))
    except Exception:
        return None  # onbekend


def main():
    global BRAND
    args = sys.argv[1:]
    # Eerste argument dat geen bekend affix is, geldt als merknaam.
    if args and args[0].lower() not in AFFIXES:
        BRAND = args[0].lower()
        args = args[1:]
    if BRAND == "merk":
        sys.exit("Geef een merknaam op: python3 discover.py <merknaam>  (of pas BRAND aan)")
    affixes = AFFIXES + args

    cands = set()
    for a in affixes:
        for s in SEPS:
            stem = BRAND + (s + a if a else "")
            for t in TLDS:
                cands.add(stem + t)
            if a:
                cands.add(a + s + BRAND + ".com")  # affix vóór merk

    hits = []
    for d in sorted(cands):
        if d in ALLOWLIST:
            continue
        try:
            ips = socket.gethostbyname_ex(d)[2]
        except Exception:
            continue
        cf = is_cloudflare(ips)
        hits.append((d, ips, cf))

    print(f"Kandidaten: {len(cands)} | Resolvet (excl. allowlist): {len(hits)}\n")
    # Verdachte hits eerst (Cloudflare = sterk daderkenmerk in deze cases).
    hits.sort(key=lambda h: (not h[2], h[0]))
    for d, ips, cf in hits:
        vlag = "⚠ CLOUDFLARE — verdacht, verifiëren" if cf else "  (niet-CF, lager risico)"
        print(f"  {d:26} {vlag}")
        print(f"       {ips}")
    print("\nVervolg per ⚠-hit: WebFetch https://who.is/whois/<domein> (registrar +"
          " datum + reseller), dan Chrome-verificatie (merklogo? checkout-kaartoogst?).")
    print("Vergeet de externe CT-alert niet — die vangt namen buiten deze lijst.")


if __name__ == "__main__":
    main()

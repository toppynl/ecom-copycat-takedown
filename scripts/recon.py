#!/usr/bin/env python3
"""DNS-recon voor een (vermoedelijk) namaakdomein.

Gebruik:  python3 recon.py <domein>

Doet uitsluitend DNS-lookups (A/AAAA/NS/MX/TXT) + Cloudflare-detectie.
WHOIS/RDAP gaat NIET via dit script (port 43 en directe HTTP zijn in de
sandbox geblokkeerd): haal registrar, abuse-contact, registratiedatum en
reseller op via WebFetch op https://rdap.org/domain/<domein> en zo nodig
https://lookup.icann.org/.
"""
import ipaddress
import json
import subprocess
import sys
from datetime import datetime, timezone

try:
    import dns.resolver
except ImportError:
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", "dnspython"],
        check=False,
    )
    import dns.resolver

# Gepubliceerde Cloudflare IPv4-ranges (https://www.cloudflare.com/ips/)
CLOUDFLARE_V4 = [
    "173.245.48.0/20", "103.21.244.0/22", "103.22.200.0/22", "103.31.4.0/22",
    "141.101.64.0/18", "108.162.192.0/18", "190.93.240.0/20", "188.114.96.0/20",
    "197.234.240.0/22", "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/13",
    "104.24.0.0/14", "172.64.0.0/13", "131.0.72.0/22",
]


def query(domain, rtype):
    try:
        return [r.to_text() for r in dns.resolver.resolve(domain, rtype)]
    except Exception:
        return []


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    domain = sys.argv[1].strip().lower()
    for prefix in ("http://", "https://"):
        domain = domain.removeprefix(prefix)
    domain = domain.split("/")[0].removeprefix("www.")

    result = {
        "domein": domain,
        "tijdstip_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "a_records": query(domain, "A"),
        "aaaa_records": query(domain, "AAAA"),
        "nameservers": query(domain, "NS"),
        "mx_records": query(domain, "MX"),
        "txt_records": query(domain, "TXT")[:20],
    }

    nets = [ipaddress.ip_network(n) for n in CLOUDFLARE_V4]
    cf_by_ip = any(
        any(ipaddress.ip_address(ip) in net for net in nets)
        for ip in result["a_records"]
    )
    cf_by_ns = any("cloudflare" in ns.lower() for ns in result["nameservers"])
    result["cloudflare"] = cf_by_ip or cf_by_ns
    result["geen_mx"] = not result["mx_records"]

    print(json.dumps(result, indent=2, ensure_ascii=False))
    print()
    if result["cloudflare"]:
        print("→ ACHTER CLOUDFLARE: origin-host verborgen. Cloudflare-abusemelding is")
        print("  primair kanaal (proxy stoppen + host-onthulling via report-ID).")
    elif result["a_records"]:
        print("→ NIET achter Cloudflare: A-record wijst waarschijnlijk direct naar de")
        print("  host. Zoek de ASN/host + abuse-adres op via WebFetch:")
        print(f"  https://rdap.org/ip/{result['a_records'][0]}")
    else:
        print("→ Geen A-records: domein resolvet niet (mogelijk al geschorst of")
        print("  nog niet actief). Controleer de spelling en check RDAP.")
    if result["geen_mx"]:
        print("→ GEEN MX-record: domein ontvangt geen e-mail — indicatie van een")
        print("  pure fraude-façade. Vermeld dit in het dossier.")
    print()
    print("VOLGENDE STAP (niet via dit script): WebFetch op")
    print(f"  https://rdap.org/domain/{domain}")
    print("voor registrar, abuse-contact, registratiedatum, registry-ID, reseller.")


if __name__ == "__main__":
    main()

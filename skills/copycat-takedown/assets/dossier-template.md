# Takedown-dossier — {{DOMEIN}}

> Aangemaakt: {{DATUM}} · Status: **lopend**
> Eén-plek-waarheid voor deze case. Elke respons/statuswijziging hier bijwerken.

## 0. Zaakgegevens

| Veld | Waarde |
|---|---|
| **Namaakdomein** | `{{DOMEIN}}` |
| **Ons echte domein** | `{{ECHT_DOMEIN}}` |
| **Rechthebbende** | `{{RECHTHEBBENDE}}` |
| **Contactpersoon** | `{{MELDER}}, {{ROL}}` |
| **E-mailadres** | `{{EMAIL}}` |
| **Merkregistratie** | `{{MERKREG}}` |
| **Merknaam** | `{{MERK}}` |
| **Datum melding** | {{DATUM}} |

## 1. Technische bevindingen (recon {{DATUM}})

- **A-records:** {{A_RECORDS}}
- **Nameservers:** {{NAMESERVERS}}
- **MX:** {{MX_STATUS}}
- **Cloudflare:** {{CLOUDFLARE_JA_NEE}} → {{STRATEGIE_GEVOLG}}

### WHOIS/RDAP

- **Registrar:** {{REGISTRAR}} — abuse: {{REGISTRAR_ABUSE}}
- **Geregistreerd:** {{REG_DATUM}} {{KWADE_TROUW_NOTITIE}}
- **Verloopt:** {{EXPIRY}}
- **Registrant:** {{REGISTRANT_STATUS}}
- **Registry Domain ID:** {{REGISTRY_ID}}
- **Reseller:** {{RESELLER}}
- **Origin-host:** {{HOST}} — abuse: {{HOST_ABUSE}}
- **Cloudflare-report-ID:** {{CF_REPORT_ID}}
- **Betaalmethode op site:** {{PSP}}

### Status live site ({{DATUM}} {{TIJD}})

{{SITE_STATUS}}

## 2. Bewijs

- [ ] Screenshot homepage (volledige pagina, URL + datum/tijd zichtbaar)
- [ ] Screenshots productpagina's met merk/logo/foto-misbruik
- [ ] Screenshot van elke plek waar merknaam "{{MERK}}"/beeldmerk verschijnt
- [ ] Archive.org-capture: {{ARCHIVE_URL}}
- [ ] DNS-bevindingen opgeslagen (§1)
- [ ] Inventaris overgenomen teksten/foto's van {{ECHT_DOMEIN}}

## 3. Voortgang meldingen

| Melding | Kanaal | Klaargezet | Verstuurd | Referentie/ticket | Status |
|---|---|---|---|---|---|
| Registrar | {{REGISTRAR_ABUSE}} | ☐ | ☐ | | |
| Cloudflare abuse | webformulier | ☐ | ☐ | | |
| Google Safe Browsing | webformulier | ☐ | ☐ | | |
| Microsoft SmartScreen | webformulier | ☐ | ☐ | | |
| Hostingprovider | {{HOST_ABUSE}} | ☐ | ☐ | | |
| Reseller | {{RESELLER_ABUSE}} | ☐ | ☐ | | |
| Betaalprovider | {{PSP_ABUSE}} | ☐ | ☐ | | |
| Klantwaarschuwing | {{ECHT_DOMEIN}} + social | ☐ | ☐ | | |
| Fraudehelpdesk | fraudehelpdesk.nl | ☐ | ☐ | | |
| Politie-aangifte | — | ☐ | ☐ | | |

## 4. Openstaande acties gebruiker

- [ ] Gmail-drafts verzenden: {{DRAFT_LIJST}}
- [ ] Webformulieren indienen: Cloudflare, Safe Browsing, SmartScreen
- [ ] {{OVERIGE_ACTIES}}

## 5. Afronding (na schorsing)

- [ ] Bewijs definitief opslaan (lokaal + back-up) — ook nodig bij heroprichting/aangifte
- [ ] Schorsingsbevestiging van registrar bewaren in dossier
- [ ] Klantwaarschuwing aanpassen/verwijderen
- [ ] Check op meegeschorste zusterdomeinen van dezelfde dader
- [ ] Fraudehelpdesk-melding (optioneel, landelijke registratie)
- [ ] Politie-aangifte (alleen bij schade/gedupeerden of juridische escalatie)
- [ ] Monitoring: Google Alert + periodieke check op nieuwe "{{MERK}}"-domeinen
- [ ] Overweeg structurele merkbewaking via merkgemachtigde (intellectueeleigendom.nl, ID 83821)

## 6. Logboek

| Datum | Gebeurtenis |
|---|---|
| {{DATUM}} | Dossier aangemaakt, recon uitgevoerd, meldingen klaargezet |

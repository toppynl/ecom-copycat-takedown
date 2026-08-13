# Meldingsteksten — merk-copycat takedown (merk-neutraal)

Alle templates voor §3–§6. Vul de plaatshouders met de zaakgegevens (uit
SKILL.md) en de recon-data; laat geen `{{...}}` staan in de eindversie.
Onbekend gegeven → "[volgt — nog niet bekend]" en later bijwerken.

**Plaatshouders — zaakgegevens (eenmalig, uit SKILL.md):**

| Plaatshouder | Betekenis |
|---|---|
| `{{MERK}}` | de merknaam |
| `{{ECHT_DOMEIN}}` | het echte domein van het merk |
| `{{RECHTHEBBENDE}}` | juridische naam rechthebbende |
| `{{MELDER}}` | contactpersoon (naam) |
| `{{ROL}}` | functie/rol van de melder |
| `{{EMAIL}}` | e-mailadres melder |
| `{{MERKREG}}` | merkregistratie (bijv. "EU trademark no. 000000000, classes 35 & 39, registered dd-mm-yyyy" of Benelux/BOIP/nationaal nummer) |

**Plaatshouders — per case (uit recon):**

| Plaatshouder | Betekenis |
|---|---|
| `{{DOMEIN}}` | het namaakdomein |
| `{{REG_DATUM}}` | registratiedatum domein |
| `{{REGISTRY_ID}}` | Registry Domain ID (of "niet zichtbaar in publieke WHOIS") |
| `{{REGISTRAR}}` | registrarnaam |
| `{{HOST_ASN}}` | ASN + naam host |
| `{{CF_REPORT_ID}}` | Cloudflare report-ID (uit hun reply) |
| `{{BEWIJS}}` | link(s) archive.org-capture / screenshots |

---

## 1. Cloudflare abuse (webformulier — invulklare tekst)

Formulier: https://abuse.cloudflare.com/ → *Trademark* of *Phishing & Malware*.
WHOIS-disclosure registrant: https://abuse.cloudflare.com/registrar_whois

**Onderwerp:** Trademark infringement & fraudulent copycat shop — {{DOMEIN}}

```
To: Cloudflare Trust & Safety

I am reporting the website hosted/proxied via Cloudflare at:
  https://www.{{DOMEIN}}/

This is a fraudulent copycat of our legitimate store {{ECHT_DOMEIN}}. It
impersonates our brand to deceive consumers.

Trademark basis:
  - "{{MERK}}" is a registered trademark ({{MERKREG}}), held by
    {{RECHTHEBBENDE}}.
  - The site reproduces our brand name/logo (per attached evidence) without
    authorisation, and/or the domain incorporates our mark.

Nature of abuse:
  - Trademark infringement
  - Consumer fraud / impersonation of a legitimate retailer
  - The domain "{{DOMEIN}}" is confusingly similar to our brand and domain
    {{ECHT_DOMEIN}}.
  - Bad faith: the domain was registered on {{REG_DATUM}}, long after our
    trademark, to imitate our brand. [If card-skimming: the checkout collects
    raw card number/expiry/CVC with no legitimate payment processor.]

Evidence:
  - Timestamped archive: {{BEWIJS}}
  - Screenshots of the infringing pages
  - Our trademark registration: {{MERKREG}}
  - Our legitimate site: https://{{ECHT_DOMEIN}}

Requested action:
  - Cease proxying/hosting the infringing site, and
  - Disclose the origin host and registrant data so we can pursue a full
    takedown.

Reporter:
  {{MELDER}}, {{ROL}}
  {{EMAIL}}
  on behalf of {{RECHTHEBBENDE}}, rights holder of the "{{MERK}}" trademark
```

---

## 2. Registrar — lokale registrar (e-mail, lokale taal)

Naar het abuse-/security-adres uit WHOIS/RDAP. Sommige registrars hebben een
eigen abuse-webformulier — check hun site. (NL-voorbeeld hieronder; vertaal naar
de taal van de registrar.)

**Onderwerp:** Merkinbreuk & fraude — {{DOMEIN}} (geregistreerd via {{REGISTRAR}})

```
Geachte heer/mevrouw,

Wij melden misbruik van een domein dat via {{REGISTRAR}} is geregistreerd:

  Domein:        {{DOMEIN}}
  Geregistreerd: {{REG_DATUM}}
  Registry ID:   {{REGISTRY_ID}}

Dit domein wordt gebruikt voor een namaakwebshop die zich voordoet als onze
legitieme winkel {{ECHT_DOMEIN}}, en maakt inbreuk op ons geregistreerde merk
"{{MERK}}" ({{MERKREG}}, houder {{RECHTHEBBENDE}}).

Aard van het misbruik:
  - Merkinbreuk: het domein/de site bootst ons merk "{{MERK}}" na.
  - Consumentenfraude / impersonatie van een bestaande retailer.
  - Kwade trouw: het domein is pas op {{REG_DATUM}} geregistreerd.
  - "{{DOMEIN}}" is verwarrend gelijk aan ons merk en domein {{ECHT_DOMEIN}}.

Dit is in strijd met uw Acceptable Use / Anti-Abuse Policy. Wij verzoeken u:
  1. het domein {{DOMEIN}} te schorsen/op te heffen, en
  2. de geregistreerde registrant-gegevens vrij te geven.

Bewijs:
  - Merkregistratie {{MERKREG}} ({{RECHTHEBBENDE}})
  - Onze legitieme site: https://{{ECHT_DOMEIN}}
  - Screenshots / archief: {{BEWIJS}}

Met vriendelijke groet,
{{MELDER}}, {{ROL}}
{{EMAIL}}
namens {{RECHTHEBBENDE}}, houder van het merk "{{MERK}}"
```

---

## 3. Registrar / host / reseller — buitenlands (e-mail, EN)

**Onderwerp:** Trademark infringement & fraud — {{DOMEIN}} (via {{REGISTRAR}})

```
Dear Sir or Madam,

We are reporting abuse of a domain registered/hosted via {{REGISTRAR}} /
{{HOST_ASN}}:

  Domain:      {{DOMEIN}}
  Registered:  {{REG_DATUM}}
  Registry ID: {{REGISTRY_ID}}

This domain hosts a counterfeit webshop impersonating our legitimate store
{{ECHT_DOMEIN}}, infringing our registered trademark "{{MERK}}" ({{MERKREG}},
owner {{RECHTHEBBENDE}}).

Nature of the abuse:
  - Trademark infringement: it imitates our brand "{{MERK}}".
  - Consumer fraud / impersonation of an existing retailer.
  - Bad faith: registered on {{REG_DATUM}}, long after our trademark.
  - [If card-skimming: the checkout collects raw card number/expiry/CVC with no
    legitimate payment processor — card data is harvested directly.]
  - "{{DOMEIN}}" is confusingly similar to our brand and domain {{ECHT_DOMEIN}}.

This violates your Acceptable Use / Anti-Abuse Policy. We request that you:
  1. suspend or delete the domain / remove the site, and
  2. disclose the (currently redacted) registrant data.

[Host only — via Cloudflare disclosure:] Identified via Cloudflare Trust &
Safety, report ID {{CF_REPORT_ID}}.

Evidence:
  - Trademark registration {{MERKREG}} ({{RECHTHEBBENDE}})
  - Our legitimate site: https://{{ECHT_DOMEIN}}
  - Screenshots / archive: {{BEWIJS}}

Kind regards,
{{MELDER}}, {{ROL}}
{{EMAIL}}
on behalf of {{RECHTHEBBENDE}}, owner of the "{{MERK}}" trademark
```

---

## 4. Betaalprovider / PSP (e-mail, EN) — alleen na checkout-verificatie

**Eerst verifiëren welke PSP er écht achter zit** (checkout-netwerkverkeer, niet
de footer-logo's). Geen PSP-script → deze melding vervalt; noteer "rauwe
kaartoogst" als bewijs in de phishingmeldingen.

| PSP | Kanaal |
|---|---|
| Stripe | supportformulier: https://support.stripe.com/contact ("report a fraudulent business") |
| PayPal | https://www.paypal.com/us/webapps/mpp/security/report-problem |
| Mollie | supportkanaal op mollie.com |
| Adyen | abuse@adyen.com |

```
Subject: Fraudulent merchant using your payment services — {{DOMEIN}}

The site {{DOMEIN}} is a copycat fraud shop impersonating {{ECHT_DOMEIN}} and
our trademark "{{MERK}}" ({{MERKREG}}, owner {{RECHTHEBBENDE}}). It appears to
process payments via your service. Please review and suspend the merchant.
Evidence: {{BEWIJS}} — {{MELDER}}, {{ROL}}, {{EMAIL}}.
```

---

## 5. Google Safe Browsing (webformulier)

Formulier: https://safebrowsing.google.com/safebrowsing/report_phish/

```
URL: https://www.{{DOMEIN}}/

Reason: This site impersonates the legitimate retailer {{ECHT_DOMEIN}}, using
the registered "{{MERK}}" brand ({{MERKREG}}) to defraud consumers. It is a
copycat fraud shop, not affiliated with the rights holder. [If applicable: the
checkout harvests raw payment card data.]
```

## 6. Microsoft SmartScreen (webformulier)

Formulier: https://www.microsoft.com/en-us/wdsi/support/report-unsafe-site —
zelfde toelichting; dreiging "Phishing", taal van de site instellen.

---

## 7. Klantwaarschuwing (voor {{ECHT_DOMEIN}} + social)

```
⚠️ Let op: er circuleert een nepwebshop {{DOMEIN}} die zich voordoet als {{MERK}}.
Deze site heeft niets met ons te maken. Bestel uitsluitend via {{ECHT_DOMEIN}}.
[Bij kaartskimmer: De afrekenpagina steelt creditcardgegevens — al betaald? Bel
je bank en blokkeer je kaart.] Iets besteld via de nepsite? Meld het bij het
lokale fraudemeldpunt.
```

---
name: ecom-copycat-takedown
description: >-
  Takedown-draaiboek voor namaak-/phishingwebshops die het merk van de gebruiker
  misbruiken. Gebruik deze skill ALTIJD zodra iemand een copycat-, namaak-, nep-
  of phishingsite meldt, een verdacht domein noemt dat op het eigen merk lijkt,
  of zegt iets als "nieuwe namaaksite", "fake webshop", "nepshop", "iemand doet
  zich voor als ons", "merk misbruikt", "takedown" of "haal [domein] offline" —
  ook als het woord "skill" of "dossier" niet valt. De skill doet DNS-recon en
  WHOIS/RDAP, ontdekt gelieerde copycats, legt bewijs vast, vult een dossier in
  en zet meldingen klaar voor registrar/host/reseller, Cloudflare, Google Safe
  Browsing en Microsoft SmartScreen — binnen de grenzen die aan het begin met de
  gebruiker worden afgestemd (§0).
---

# Merk-copycat takedown (merk-neutraal draaiboek)

Merk-neutrale sjabloonversie: doorloop eenmalig het startgesprek (§0) en vul de
zaakgegevens in, daarna werkt de flow voor elk merk.

## Drie doelen (houd deze altijd in het achterhoofd)

Deze skill dient drie doelen tegelijk. Doel 1 is de directe opdracht; doel 2 en 3
lopen op de achtergrond mee bij elke case.

1. **De gemelde copycat/nepshop offline krijgen** — de kernopdracht (§1–§7).
2. **Gelieerde copycats vinden** — daders werken vaak in clusters, dus zoek bij
   elke case actief naar zusterdomeinen (§8). Eén site neerhalen terwijl er drie
   naast draaien is halve winst.
3. **Dit publieke draaiboek beter maken** — merk je dat een kanaal, tactiek of
   volgorde aantoonbaar beter werkt dan wat hier staat, koppel dat dan terug
   (§9). **Let op de lat:** dit is een openbaar, gedeeld project en de eigenaar
   wil géén stortvloed aan kleine of speculatieve suggesties. Stel alléén een
   feature request op bij een **echt, onderbouwd inzicht** — reproduceerbaar,
   met bewijs, dat de aanpak wezenlijk verbetert. Twijfel je of het die lat
   haalt, noteer het dan wél in het dossier maar dien het (nog) niet in. Kwaliteit
   boven kwantiteit.

## §0 Startgesprek — eenmalig afstemmen (doe dit eerst)

Deze skill kan veel zelf doen, maar wát er automatisch mag en wat eerst langs de
gebruiker moet, verschilt per persoon, per organisatie en per systeemtoegang.
Begin daarom altijd met een kort startgesprek en leg de afspraken vast bovenaan
het dossier. Ga niet zelfstandig in iemands mailbox, browser of andere
persoonlijke systemen kijken zonder dat dit hier expliciet is afgesproken.

Stem minstens deze punten af:

1. **Automatiseringsniveau.** Wat mag de skill zelfstandig uitvoeren en wat wil
   de gebruiker eerst zelf zien/goedkeuren? Denk aan: recon en ontdekking
   (meestal veilig, geen neveneffecten), concepten opstellen, webformulieren
   vóórinvullen. Verzenden, indienen en publiceren blijven altijd bij de
   gebruiker, tenzij die uitdrukkelijk anders vraagt.
2. **Mailboxtoegang.** Mag de skill zelf de mailbox doorzoeken op reacties van
   registrar/host/Cloudflare/meldpunten (§3)? Zo ja: alleen gericht zoeken op
   die afzenders, niets anders. Zo nee: prima — dan levert de skill per melding
   een lijstje "let op deze afzenders in je inbox" en werkt de gebruiker de
   statussen zelf bij. Scrape nooit persoonlijke of ongerelateerde inhoud.
3. **Browsertoegang.** Is er een browser-tool (bijv. Claude in Chrome) om
   screenshots te maken, archive.org te triggeren en formulieren voor te
   invullen? Zo niet, dan levert de skill die stappen als handmatige actiepunten
   met invulklare teksten.
4. **Reikwijdte van de meldingen.** Alleen het merk van de gebruiker, of ook
   gerelateerde infrastructuur (skimmer-/exfil-domeinen)? De gebruiker beslist.
5. **Escalatie & publiek.** Klantwaarschuwing, fraudemeldpunt en politie zijn
   optioneel en volgen alleen op verzoek (zie §5–§6).

Werk daarna in redelijk zelfstandige doorlopen: voer uit wat is afgesproken,
stel niet bij elke stap opnieuw een vraag, en sluit af met één compact overzicht
van wat klaarstaat en welke handelingen (verzenden, indienen, beslissen) nog aan
de gebruiker zijn.

## Eenmalig invullen — vaste zaakgegevens

Vul dit blok één keer met de gegevens van het merk/de rechthebbende. Alle
meldingen gebruiken deze waarden. Staat een veld nog op `[…]`, vraag het dan
éénmalig.

| Veld | Waarde (invullen) |
|---|---|
| Merknaam | `[MERK]` |
| Ons echte domein | `[echt-domein.nl]` |
| Rechthebbende (juridische naam) | `[Bedrijf B.V.]` |
| Contactpersoon | `[Voor- en achternaam]` |
| Functie/rol (voor formulieren met "Title") | `[bijv. Brand Manager]` |
| E-mailadres | `[naam@echt-domein.nl]` |
| Merkregistratie | `[bijv. EU-/Benelux-/nationaal merknr 000000000 — beeldmerk "MERK", kl. 35 & 39, ingeschreven dd-mm-jjjj]` |
| Echt vestigingsadres | `[Straat 1, 0000 AA Plaats]` (om verzonnen adressen op nepsites te herkennen) |
| Merkgemachtigde (optioneel) | `[naam / bureau]` |

Zodra dit is ingevuld heeft elke nieuwe case alleen nog het **namaakdomein** nodig.

## Aanpak en volgorde (richtlijn, geen wet)

Onderstaande volgorde werkt in de praktijk vaak goed, maar is een startpunt —
geen dogma. Weeg per case af en pas aan.

1. **Recon + bewijs** — parallel, meteen (§1–2). Melden kan al vóórdat de site
   bereikbaar is; wacht dus nooit op een werkende site om te beginnen.
2. **Registrar + Cloudflare + Safe Browsing/SmartScreen** (§3–4).
   *Werkhypothese: de **registrar** is vaak het beslissende kanaal — die zit hoog
   in de keten en kan een domein schorsen ongeacht host of reseller. Toets dit
   per case; het is geen garantie (sommige registrars weigeren, of verwijzen naar
   een eigen formulier). Zie §9 over het terugkoppelen van wat wél/niet werkt.*
3. **Host + reseller + PSP** — zodra bekend uit recon/Cloudflare-respons (§3).
4. **Dossier opleveren + monitoring** (§7–8).
5. **Optioneel, alleen op verzoek:** klantwaarschuwing (§6), fraudemeldpunt/
   politie (§5).

Maak bij de start een takenlijst met de relevante fasen.

## §1 Technische recon

```bash
python3 scripts/recon.py <namaakdomein>
```

Verzamelt A/AAAA-records, nameservers, MX en TXT, en detecteert Cloudflare.
Daarna:

- **WHOIS via RDAP/who.is:** WebFetch in deze volgorde —
  (1) `https://who.is/whois/<domein>`, (2) `https://rdap.org/domain/<domein>`,
  (3) ICANN Lookup. Zoek: registrar + IANA-ID, abuse-e-mail, registratiedatum,
  registry domain ID, registrantstatus (redacted?), reseller. Niet achter
  Cloudflare → zoek de host via `https://rdap.org/ip/<A-record-IP>`. Gebruik
  géén `whois`/`curl` — port 43 en directe fetches zijn vaak geblokkeerd;
  WebFetch is de route.
- **Registratiedatum duiden:** een jong domein tegenover een merk van jaren oud
  is een sterk kwade-trouw-argument; benoem dit in elke melding.

Interpretatie: achter Cloudflare → origin-host verborgen, Cloudflare-abuse is het
kanaal voor proxy-stop + eventuele host-onthulling. Lokale registrar → melding in
de lokale taal met verwijzing naar hun Anti-Abuse Policy. Geen MX → domein
ontvangt geen mail (fraude-façade).

## §2 Bewijs vastleggen (vóór alles wat de site kan doen verdwijnen)

1. **Archive.org**: via de browser-tool naar
   `https://web.archive.org/save/https://<namaakdomein>/`; noteer de snapshot-URL
   (met tijdstempel). WebFetch op de save-URL wordt vaak geblokkeerd; een browser
   is betrouwbaarder.
2. **Screenshots** (browser, opslaan naar schijf): homepage, productpagina's en
   elke plek waar merknaam/logo/foto's van het echte merk verschijnen.
3. **Contact-/Over-ons-pagina**: nepshops tonen vaak een lokaal ogend adres om
   legitiem te lijken. Vergelijk met het **echte vestigingsadres** uit de
   zaakgegevens; wijkt het af, behandel het dan als **verzonnen** ("a fabricated
   address to appear legitimate"). Noteer verder: absurde kortingen (~70%+),
   lorem-ipsum-resten, ontbrekend e-mailadres/telefoonnummer, buitenlandse
   adresnotatie.
4. **PSP verifiëren via de checkout — vertrouw nooit footer-logo's.** Ga (zonder
   iets in te vullen) naar de afrekenpagina en lees met read_network_requests
   welke betaalscripts laden: js.stripe.com = Stripe, mollie.com = Mollie,
   adyen.com = Adyen. Géén PSP-script + kaal kaartnummer/expiry/CVC-formulier
   (bijv. WooCommerce jquery.payment/credit-card-form.min.js) = **rauwe
   kaartoogst / kaartskimmer**. Let ook op een extern script van een vreemd
   domein — dat kan de exfil-endpoint zijn. Dan vervalt de PSP-melding en is dit
   juist hard bewijs voor de phishing-classificatie; benoem het expliciet.
5. Site **offline** bij controle: noteer status + tijd; melden gaat gewoon door.

## §3 Meldingen klaarzetten

Alle teksten staan in `references/meldingen.md` — lees dat bestand en vul de
plaatshouders met de zaakgegevens + recon-data. Twee soorten output:

**A. E-mailconcepten (maak drafts met de mail-tools, niet versturen):**
registrar (hoogste prioriteit), hostingprovider (zodra host bekend), reseller
(als die in de keten zit), betaalprovider (alleen na checkout-verificatie dat er
een echte PSP is). Lokale partijen krijgen de lokale-taal-template, buitenlandse
de Engelse. Let op: sommige registrars weigeren e-mail en eisen een
webformulier — check dat en zet het dan als formulier klaar.

**Belangrijk bij drafts:** mailclients linkificeren domeinachtige tekst in het
platte-tekstdeel en wikkelen die in redirect-URL's — dat oogt zelf als phishing.
Lever daarom ALTIJD ook een `htmlBody` aan met nette `<a href>`-links en
domeinnamen als gewone tekst. Controleer de opgeslagen draft en laat de gebruiker
het concept visueel nakijken vóór verzenden.

**B. Webformulieren (invulklare tekst + link; via de browser indienen):**
Cloudflare abuse (https://abuse.cloudflare.com/ → Phishing/Trademark),
Google Safe Browsing (https://safebrowsing.google.com/safebrowsing/report_phish/),
Microsoft SmartScreen (https://www.microsoft.com/en-us/wdsi/support/report-unsafe-site).

**Verwachtingen managen:** het aantal drafts verschilt per case (geen reseller,
host nog verborgen, sommige kanalen zijn formulieren). Leg kort uit welke kanalen
via formulier lopen en welke mails nog volgen.

**Reacties volgen.** Registrar/host/Cloudflare/meldpunten reageren per e-mail.
Als in het startgesprek (§0) is afgesproken dat de skill de mailbox mag
doorzoeken, doe dat dan gericht op die afzenders en werk het dossier bij. Is dat
níét afgesproken, lever dan per melding een "let op deze afzenders"-lijstje en
laat de gebruiker de reacties zelf plakken; werk het dossier bij op basis
daarvan. Aandachtspunt bij Cloudflare: de eerste mail is enkel een bevestiging
met report-ID; een eventuele host-onthulling volgt later en is geen garantie —
Cloudflare stuurt de klacht + origin-IP sowieso door naar host en eigenaar.
Blijft onthulling uit, dan kan de host soms via historische DNS gevonden worden
(viewdns.info, SecurityTrails). Zodra de host bekend is: host-draft aanmaken met
verwijzing naar het report-ID.

## §4 Snelle schadebeperking

Safe Browsing en SmartScreen zorgen voor een rode waarschuwing in browsers en
beperken de schade al tijdens de takedown. Vermeld de merkregistratie en dat de
site een niet-gelieerde copycat is.

## §5 Meldpunten en politie (optioneel — alleen op verzoek)

Deze stap is **niet standaard**. Doe dit alleen als er daadwerkelijk schade of
gedupeerden zijn én de gebruiker het wil. Zet ze dan als actiepunt in het
dossier; de gebruiker onderneemt/bevestigt zelf. Pas de kanalen aan het land van
de rechthebbende aan. Voorbeelden voor Nederland: Fraudehelpdesk
(fraudehelpdesk.nl / zakelijk fhdzakelijk.nl), politie-aangifte (bij
schade/gedupeerden), Stichting Aanpak Fakewebshops, ACM/ConsuWijzer.

## §6 Klantwaarschuwing (optioneel — alleen op verzoek)

Alleen relevant als de gebruiker klanten actief wil waarschuwen. Concepttekst
staat in `references/meldingen.md`; vul merk + domein in en lever aan. Publiceren
beslist de gebruiker. Bij een kaartskimmer kun je adviseren niet te lang te
wachten, maar de keuze blijft aan de gebruiker.

## §7 Dossier opleveren

Gebruik `assets/dossier-template.md`. Vul alle secties, sla op als
`takedown-dossier-<domein>.md` en lever het bestand. Het dossier is de
één-plek-waarheid; werk elke vervolgactie hierin bij. Neem bovenin ook de
afspraken uit het startgesprek (§0) op. Sluit af met een compact overzicht:
gedaan / drafts te verzenden / formulieren in te dienen / open beslissingen.

## §8 Opvolging, monitoring en copycats ontdekken

- **Copycats ontdekken:**
  ```bash
  python3 scripts/discover.py <merknaam>
  ```
  Genereert honderden permutaties (merk × algemene affixes × koppeltekens ×
  TLD's), resolvet ze, filtert de allowlist en markeert Cloudflare-treffers als
  verdacht. Verifieer elke ⚠-hit via `who.is` + browser. Voeg merk-/sectorspecifieke
  affixes toe als extra argumenten. Meerlaags, want geen methode dekt alles:
  (1) `discover.py`, (2) **Certificate Transparency** (crt.sh/CertSpotter of een
  merkbewakingsdienst — laat de gebruiker die alert instellen; een alertmail kan
  de skill oppikken als mailboxtoegang is afgesproken), (3) urlscan.io-pivot op
  paginatitel/favicon, (4) merkbewaking via de merkgemachtigde.
- **Follow-up:** een werkbaar ritme is de eerste dagen dagelijks, daarna om de
  ~48 uur tot ~2 weken — pas aan naar wens. Gebruik scheduled-task-tools die in
  dezelfde sessie terugkomen. Elke check: mailbox (indien afgesproken),
  sitestatus, `discover.py`, dossier bijwerken. Lange stilte → escalatie
  overwegen (rappel registrar, takedowndienst, merkgemachtigde).
- **Na schorsing:** afrondingschecklist in het dossier-sjabloon.

## §9 Leren & terugkoppelen naar GitHub (dit is een levend, gedeeld draaiboek)

De aanpak hierboven is gebaseerd op wat tot nu toe werkte, niet op zekerheden.
Toets per case welk kanaal daadwerkelijk tot schorsing leidde en hoe lang het
duurde, en noteer dat in het dossier. Vermijd stellige claims ("altijd",
"bewezen"); formuleer als werkhypothese.

**De lat ligt hoog (zie ook doel 3 bovenaan).** Dit is een openbaar draaiboek en
de eigenaar wil geen stroom aan kleine of onzekere suggesties. Koppel alléén iets
terug als het een **echt, onderbouwd inzicht** is: reproduceerbaar, met bewijs,
en het verbetert de aanpak wezenlijk (sneller, effectiever, of werkt waar de
huidige stappen falen). Alles daaronder blijft in het dossier staan als notitie,
maar wordt géén issue. Bij twijfel: niet indienen.

**Haalt een ontdekking die lat wel** (een kanaal, formulier, tactiek of volgorde
die niet — of anders — in dit draaiboek staat en die aantoonbaar hielp), koppel
dat dan terug als **feature request (GitHub-issue)**. Doe dat zo:

1. **Documenteer het eerst in het dossier**: wat is geprobeerd, welk kanaal
   werkte, doorlooptijd, en geanonimiseerd bewijs (casenummer/bevestiging).
2. **Stel een feature request op** volgens het sjabloon
   `.github/ISSUE_TEMPLATE/new-takedown-method.md`. Vul elk kopje in op basis van
   de case. **Verwijder alle privacygevoelige gegevens** (namen, e-mailadressen,
   order-/klantgegevens, kaartnummers) — beschrijf skimmers functioneel, plak
   nooit gestolen data.
3. **Dien het in.** Twee routes, afhankelijk van wat is afgesproken/beschikbaar:
   - **Automatisch** (als de GitHub-CLI `gh` beschikbaar en ingelogd is):
     ```bash
     gh issue create --repo toppynl/ecom-copycat-takedown \
       --title "[Methode] <korte omschrijving>" \
       --label "takedown-method,enhancement" \
       --body-file <pad-naar-ingevuld-issue>.md
     ```
   - **Eén klik** (standaard, geen tooling nodig): lever de ingevulde tekst aan
     de gebruiker plus de link
     `https://github.com/toppynl/ecom-copycat-takedown/issues/new/choose`
     — de gebruiker plakt/controleert en klikt op *Submit*.
4. Indienen
   is een publieke actie: laat de gebruiker altijd eerst de inhoud nakijken en
   akkoord geven (conform §0). Verzin geen resultaten — rapporteer alleen wat
   echt is waargenomen.

Zie `CONTRIBUTING.md` voor de bredere spelregels (privacy, verantwoord gebruik,
issues vs. pull requests).

## Referenties

- `references/meldingen.md` — meldingsteksten (lokaal + EN) met plaatshouders +
  klantwaarschuwing. Lees bij §3.
- `references/voorbeeldcase.md` — geanonimiseerde afgeronde case met lessen.
- `assets/dossier-template.md` — leeg dossier-sjabloon voor §7.
- `scripts/recon.py` — DNS-recon + Cloudflare-detectie (§1).
- `scripts/discover.py` — permutatie-zeef om copycats te ontdekken (§8).

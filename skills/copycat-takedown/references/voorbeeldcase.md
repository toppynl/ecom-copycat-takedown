# Voorbeeldcase (geanonimiseerd) — afgerond, succesvol

Geanonimiseerd verloop van een echte reeks takedowns, als illustratie van hoe de
flow werkt en welke lessen erin verwerkt zijn. Namen/nummers zijn weggelaten;
het patroon is wat telt.

## Verloop (typisch)

1. **Melding binnen** van één namaakdomein (merk + variant, bijv.
   `<merk>online.com`). Recon: achter Cloudflare, geen MX, registrant redacted,
   domein enkele maanden oud → sterk kwade-trouw-signaal.
2. **Bewijs** vastgelegd (Wayback-capture + screenshots) vóór iets anders.
   Checkout gecontroleerd: bleek een kale kaartnummer/CVC-formulier zonder echte
   PSP → **kaartskimmer**, met een extern exfil-script op een niet-gerelateerd
   domein.
3. **Meldingen** de deur uit: registrar (hoogste prioriteit), Cloudflare,
   Google Safe Browsing, Microsoft SmartScreen, lokaal fraudemeldpunt.
4. **Resultaat:** in deze case schorste de **registrar** het domein binnen enkele
   dagen (registry-NXDOMAIN — het hele domein verdween). Cloudflare haalde zelf
   niets offline maar stuurde de klacht door naar host en eigenaar. (Eén
   observatie, geen garantie — toets per case welk kanaal werkt; zie §9.)
5. **Monitoring** ontdekte vervolgens **meer domeinen van dezelfde dader**
   (zelfde registrar, Cloudflare, identiek WooCommerce/Flatsome-bouwsel, zelfde
   skimmer-scriptnaam op roterende exfil-domeinen). Elk kreeg dezelfde flow.

## Lessen (als werkhypotheses, niet als wetten)

1. **De registrar leek hier het beslissende kanaal.** Die zit hoog in de keten en
   kan schorsen ongeacht host/reseller, en pakt soms zusterdomeinen mee. Een
   goede eerste gok om met prioriteit te melden — maar toets per case, want
   sommige registrars weigeren of verwijzen naar een eigen formulier.
2. **Cloudflare haalt zelf niets offline, maar stuurt door + kan de host
   onthullen.** De abusebevestiging bevat een report-ID; een latere mail kan de
   host noemen (geen garantie). Report-ID altijd bewaren voor de host-melding.
3. **Wacht niet op een werkende site.** Ook een platliggende of bot-blokkerende
   site kun je melden; bewijs vastleggen zodra hij laadt.
4. **Jonge registratiedatum = kwade-trouw-argument.** Expliciet benoemen.
5. **Verifieer de checkout, vertrouw geen footer-logo's.** Betaallogo's zijn
   vaak nep; de echte PSP (of het ontbreken ervan = kaartskimmer) blijkt uit het
   netwerkverkeer op de afrekenpagina.
6. **Daders werken in clusters.** Eén dader draait vaak meerdere varianten. Zeef
   breed met `discover.py` + een Certificate-Transparency-alert; vertrouw niet
   op een handmatig lijstje.
7. **Adres op de nepsite**: vergelijk met het echte vestigingsadres; wijkt het
   af, dan is het verzonnen — niet als "ons nagebootste adres" claimen tenzij het
   exact klopt.

Toets deze punten per case en stel ze bij op basis van wat werkt (zie §9 van
de SKILL.md): dit is een gedeeld, levend draaiboek.

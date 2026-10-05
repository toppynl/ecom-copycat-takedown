# Bijdragen aan dit draaiboek

Dit is een **levend draaiboek**: het wordt beter naarmate meer mensen delen wat
in de praktijk wel en niet werkt om een namaak-/phishingwebshop offline te
krijgen. Je hoeft geen ontwikkelaar te zijn om bij te dragen.

## Ik heb een nieuwe methode ontdekt die werkte

Open een **feature request** (GitHub-issue) via de knop **Issues → New issue →
"Nieuwe takedown-methode"**. Er verschijnt een sjabloon met vragen; vul het zo
volledig mogelijk in (wat deed je, wat was het resultaat, hoe lang duurde het,
bewijs). Feiten helpen meer dan meningen.

> Werk je met de skill in Claude? Dan kan de skill dit feature-request
> **automatisch voor je invullen** volgens hetzelfde sjabloon. Je hoeft het dan
> alleen nog in te dienen (plakken in een nieuw issue, of automatisch via de
> GitHub-CLI `gh` als je die eenmalig instelt). Zie §9 van `SKILL.md`.

## Belangrijk: privacy en veiligheid

- **Een issue gaat over de methode, niet over jouw bedrijf.** Neem geen
  bedrijfs- of zaakgegevens op: geen merknaam, contactpersoon, e-mailadres,
  vestigingsadres of merkregistratienummer, en niets uit je
  `takedown-zaakgegevens.md` of dossiers. Beschrijf partijen generiek
  ("een .nl-registrar", "een webshop in de modebranche"). Namen van
  registrar/host mogen wél — die zijn juist nuttig voor anderen.
- **Verwijder persoonsgegevens** vóór je iets indient: namen, e-mailadressen,
  order- of klantgegevens, en zeker kaartnummers/CVC. Beschrijf skimmer-scripts
  functioneel, plak geen gestolen data.
- Gebruik je de skill om het issue op te stellen? Die anonimiseert volgens
  dezelfde regels — maar controleer de tekst altijd zelf nog even vóór het
  indienen. Een issue is openbaar.
- Meld een **kwetsbaarheid in de tool zelf** niet als openbaar issue, maar via
  het beveiligingskanaal (zie de link onder "New issue").
- Gebruik dit draaiboek alleen tegen **daadwerkelijke inbreuk op je eigen merk**
  of dat van een partij die je vertegenwoordigt. Het is een verdedigingsmiddel,
  geen middel om legitieme concurrenten dwars te zitten.

## Ik wil de wijziging zelf aanleveren

Kun je overweg met GitHub? Open dan een **Pull Request** met je aanpassing in
`skills/copycat-takedown/`. Beschrijf in de PR kort welke case de wijziging
onderbouwt. Twijfel je? Begin gewoon met een issue — dan kijken we er samen naar.

## Waar wat hoort

Alles van de skill zelf staat onder `skills/copycat-takedown/`:

- `SKILL.md` — het draaiboek (de stappen).
- `references/meldingen.md` — meldingsteksten/sjablonen.
- `references/voorbeeldcase.md` — geanonimiseerde lessen.
- `scripts/` — hulpscripts (recon, copycat-ontdekking, CT-zoeker).
- `assets/dossier-template.md` — het lege dossier-sjabloon.

Daarnaast: `.claude-plugin/` bevat het plugin-manifest voor Claude Code (alleen
relevant bij wijzigingen aan de distributie, niet aan het draaiboek).

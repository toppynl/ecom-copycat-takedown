# ecom-copycat-takedown

Een **merk-neutraal draaiboek (Claude-skill/-plugin)** om namaak-/phishingwebshops
die jouw merk misbruiken zo snel mogelijk offline te krijgen. Je legt eenmalig je
merkgegevens vast, en daarna helpt de skill je per case met: technische recon
(DNS/WHOIS), het ontdekken van gelieerde copycat-domeinen, bewijs vastleggen,
een dossier bijhouden en kant-en-klare meldingen klaarzetten voor registrar,
host, Cloudflare, Google Safe Browsing en Microsoft SmartScreen. Jij houdt de
regie: verzenden, indienen en publiceren beslis en doe je zelf.

## Installatie

**Als plugin in Claude Code (aanbevolen — updates komen automatisch mee):**

```
/plugin marketplace add toppynl/ecom-copycat-takedown
/plugin install ecom-copycat-takedown@toppynl
```

**Handmatig (Cowork of andere Claude-omgevingen met skills):** kopieer de map
`skills/copycat-takedown/` naar je eigen skills-locatie (bijv.
`~/.claude/skills/copycat-takedown/`). Bij deze route haal je updates zelf op.

## Aan de slag

1. Start een gesprek en meld een verdachte site; de skill begint met een kort
   **startgesprek (§0)**: daar spreek je af wat automatisch mag en wat eerst
   langs jou gaat.
2. De skill vraagt eenmalig je **zaakgegevens** (merknaam, domein,
   rechthebbende, merkregistratie, enz.) en bewaart die in een lokaal bestand
   `takedown-zaakgegevens.md` in je werkmap — zie hieronder waarom.
3. Daarna is elke nieuwe case simpelweg: *"Deze site wil ik offline: <domein>"*.

## Waar blijven mijn bedrijfsgegevens?

Kort: **op je eigen machine.**

- Je zaakgegevens staan in `takedown-zaakgegevens.md` in je eigen werkmap —
  bewust **niet** in de skill zelf, zodat een plugin-update ze niet overschrijft
  en ze nooit in deze publieke repo terechtkomen. Commit dat bestand niet naar
  een publieke repo.
- Je gegevens verlaten je machine alleen in de **meldingen die jij zelf
  verstuurt** (registrar, host, Cloudflare, enz.) — dat is de bedoeling van de
  skill, en verzenden doe jij.
- Dien je een **feature request** in op deze repo (zie hieronder), dan gaat die
  over de *methode*, nooit over jouw bedrijf: de skill anonimiseert de tekst en
  neemt niets op uit je zaakgegevens of dossiers. Controleer dat zelf ook altijd
  even vóór je op *Submit* klikt — een issue is openbaar.

## Wat zit erin

| Bestand | Functie |
|---|---|
| `skills/copycat-takedown/SKILL.md` | Het draaiboek zelf (de stappen + het startgesprek). |
| `skills/copycat-takedown/references/meldingen.md` | Meldingsteksten/sjablonen (lokaal + Engels). |
| `skills/copycat-takedown/references/voorbeeldcase.md` | Geanonimiseerde afgeronde case met lessen. |
| `skills/copycat-takedown/assets/dossier-template.md` | Leeg dossier-sjabloon per case. |
| `skills/copycat-takedown/scripts/recon.py` | DNS-recon + Cloudflare-detectie. |
| `skills/copycat-takedown/scripts/discover.py` | Permutatie-zeef om lookalike-domeinen te vinden. |
| `skills/copycat-takedown/scripts/ct_search.py` | Certificate Transparency-zoeker (crt.sh via publieke Postgres) naar nieuwe merk-hostnamen. |
| `.claude-plugin/` | Plugin-manifest + marketplace-definitie voor Claude Code. |

## Belangrijk

- Dit is een **verdedigingsmiddel** tegen inbreuk op je eigen merk. Gebruik het
  niet tegen legitieme partijen.
- De aanpak is gebaseerd op wat tot nu toe werkte, **niet op zekerheden**. Toets
  per case en deel wat je leert (zie hieronder).
- Geen juridisch advies. Bij schade of gedupeerden: schakel waar nodig je
  merkgemachtigde of juridische hulp in.

## Bijdragen

Nieuwe methode ontdekt die een site offline hielp? Open een **feature request**
via *Issues → New issue → "Nieuwe takedown-methode"*. De skill kan dit ook
automatisch voor je invullen (zie §9 van `SKILL.md`) en doet dat geanonimiseerd —
zonder je bedrijfs- of zaakgegevens. Zie `CONTRIBUTING.md`.

## Licentie

MIT — zie `LICENSE`.

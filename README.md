# ecom-copycat-takedown

Een **merk-neutraal draaiboek (Claude-skill)** om namaak-/phishingwebshops die
jouw merk misbruiken zo snel mogelijk offline te krijgen. Je vult eenmalig je
merkgegevens in, en daarna helpt de skill je per case met: technische recon
(DNS/WHOIS), het ontdekken van gelieerde copycat-domeinen, bewijs vastleggen,
een dossier bijhouden en kant-en-klare meldingen klaarzetten voor registrar,
host, Cloudflare, Google Safe Browsing en Microsoft SmartScreen. Jij houdt de
regie: verzenden, indienen en publiceren beslis en doe je zelf.

## Wat zit erin

| Bestand | Functie |
|---|---|
| `SKILL.md` | Het draaiboek zelf (de stappen + het startgesprek). |
| `references/meldingen.md` | Meldingsteksten/sjablonen (lokaal + Engels). |
| `references/voorbeeldcase.md` | Geanonimiseerde afgeronde case met lessen. |
| `assets/dossier-template.md` | Leeg dossier-sjabloon per case. |
| `scripts/recon.py` | DNS-recon + Cloudflare-detectie. |
| `scripts/discover.py` | Permutatie-zeef om lookalike-domeinen te vinden. |

## Aan de slag

1. Gebruik dit in een Claude-omgeving die skills ondersteunt (Cowork of Claude
   Code). Laad de skill en doorloop het **startgesprek (§0)**: daar spreek je af
   wat automatisch mag en wat eerst langs jou gaat.
2. Vul eenmalig je **zaakgegevens** in bovenin `SKILL.md` (merknaam, domein,
   rechthebbende, merkregistratie, enz.).
3. Zeg vervolgens gewoon: *"Deze site wil ik offline: <domein>"*.

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
automatisch voor je invullen (zie §9 van `SKILL.md`). Zie `CONTRIBUTING.md`.

## Licentie

MIT — zie `LICENSE`.

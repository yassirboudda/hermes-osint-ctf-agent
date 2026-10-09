# World clue library

Read the file for the region your shortlist points to, in the funnel step where you
separate countries and regions (`references/country-funnel.md`). Each file starts
with a quick table of the strongest tells and ends with a "commonly confused" section
for pairs that look alike.

| File | Scope |
|---|---|
| `general.md` | Discriminators that work everywhere: driving side, plates, scripts, road paint, signs, poles, bollards, vegetation, soil, architecture, sun |
| `europe.md` | Europe, including Turkey, the Caucasus, Russia west of the Urals and the European microstates |
| `americas.md` | North, Central and South America and the Caribbean |
| `asia.md` | East, Southeast, South and Central Asia |
| `oceania.md` | Australia, New Zealand and the Pacific islands |
| `africa-middle-east.md` | Africa, the Arabian Peninsula, the Levant, Iran |
| `china.md` | Mainland China in depth: platform metadata, text, plates, vehicles, infrastructure, phenology, terrain, urban form |
| `streetview.md` | Google Street View imagery itself: camera generations, car and mount tells, coverage quirks, copyright watermark years. Only for Street View or game screenshots |

## Entry format

```markdown
### <clue name>
- Look for: exactly what to find in the image and how to recognize it
- Points to: country / region / city / type of area
- Strength: strong (a single clue reaches this level) / medium (needs one more) / weak (can only exclude or boost)
- Counterexamples: when it misleads
- Verify: how to confirm it (a tool command, a reference sheet comparison, a lookup)
- Source: general knowledge | URL checked YYYY-MM | case tag (vNNN = a casebook entry) | (unverified)
```

## Rules

- Every entry states strength and counterexamples. A clue with no known counterexample
  usually just has not misled anyone yet; that does not make it reliable.
- "Strong" needs three or more independent sources, or a regulation/standard that makes it
  true by law (a national plate format, an official script). Single-source claims say
  "(single source)"; claims nobody checked say "(unverified)" and stay weak.
- Only include clues that transfer to new photos. What one particular landmark looks like
  does not belong here; it will not help with the next photo.
- Never write a specific puzzle's place name or answer into a counterexample or note
  (that leaks answers into evaluations). Cite cases by method-level facts only.
- Infrastructure and vehicle conventions change: new plate formats, repainted road lines,
  new Street View generations. Old and new styles coexist for years. Treat "the format
  changed in year X" as a dating clue as well as a location clue.
- Strength depends on context: a plate on a moving car on a local street is stronger than
  a plate in a tourist car park or on a freight corridor; vegetation without a month is
  always weak.
- Observed or inferred clues from this library can only rank candidates on the board
  (`board.py evidence`, capped likelihood ratios). Excluding a candidate needs read text or
  a computed result (`board.py exclude`), never a library entry alone.
- Write in your own words. Community guides (Plonkit, GeoHints and similar) are good
  reading, but do not copy their text or images.

## Adding to the library

After a session with known ground truth (`photo_session.py truth`), add any clue that
decided the case or misled you, in the format above, with the case tag `case:<archive
folder timestamp>`. A misleading clue is as valuable as a decisive one: add it as a
counterexample to the entry that misled you.

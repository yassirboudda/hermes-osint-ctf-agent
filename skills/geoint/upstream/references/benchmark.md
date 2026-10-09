# Measuring the skill

Without measurement nobody knows whether a change helps. Two kinds of measurement exist here.

## 1. Every real session (the scoreboard)

When the true location of an archived photo becomes known:

```bash
python3 <skill>/scripts/photo_session.py truth "<final folder>" --latitude … --longitude … --country "…" --region "…" --source "owner"
python3 <skill>/scripts/photo_session.py scoreboard --write     # → photos/scoreboard.md and scoreboard.json
```

The scoreboard reports median error, the share of answers within 1 / 25 / 200 / 750 / 2500 km, country hit
rate, approximate world-map game score (5000·e^(−d/1492.7 km)), and **calibration**: how often "high",
"medium" and "low" confidence were actually right. If "high" is often wrong, the confidence rules are too loose.
Compare the gut call written in each report with the truth too: it shows how much the tools add.

## 2. Repeatable test sets

```bash
bench.py make-streetview --n 40 --seed 2 --out bench/sv40-seed2        # GeoGuessr-style rounds with hidden truth
bench.py prior bench/sv40-seed2 --out bench/sv40-seed2/preds_prior.json  # model-only baseline
bench.py score bench/sv40-seed2/preds_prior.json --truth bench/sv40-seed2/truth.json
```

- Rounds: a random covered country per round, a random town in it (population-weighted), the nearest official
  Street View panorama within ~1 km, a random heading, 1280×800 at 90° FOV. `truth.json` must never be shown to
  the solver.
- To evaluate the full skill, give the solver (a fresh agent with the skill) only `images/NNNN.jpg`, collect its
  answers as `{"NNNN": {"lat": …, "lon": …, "country": "XX"}}`, then score. Use the same seed to compare versions.
- Baseline already measured on `bench/sv24-seed1` (model only, consistent guess): country 58%, median 274 km,
  within 25 km 17%, within 200 km 42%, within 750 km 67%, mean score 3,507. A skilled agent should beat this
  clearly on country and region; if it does not, find out which step loses the information.

## First head-to-head (2026-10-08, 7 hard rounds from `bench/sv24-seed1`)

Rounds chosen where the models alone struggled (Ghana, Greece, Taiwan, Romania, Ecuador, Bangladesh, Japan). Fresh
agents, no uploads, answers hidden from them.

| Solver | Country right | Median error | Within 25 km | Notes |
|---|---|---|---|---|
| Learned models alone (`prior.py` point guess) | 3/7 | 2,166 km | 1/7 | confidently wrong on 4 rounds |
| Agent without the skill (own eye + web search) | 7/7 | 7.8 km | 5/7 | strong: the gut is the main engine; mean game score 4,906 |
| Agent with the skill (quick mode) | 7/7 | 4.7 km | 5/7 | closer in 5 of 7 paired rounds; Greece 5 km vs 87 km; mean game score 4,942 |

What made the difference: tool-driven confirmation (`gsv.py` sheets along a motorway corridor found the exact
road in Greece; plate crops from `detect.py` settled Ghana and Ecuador; local-language crop statistics settled
Taiwan). Where it lost (Romania 31 km vs 11 km; Tokyo 0.5 km vs 0.1 km) the margin came from a lucky or sharper final pin, not from the country or region. Small sample: rerun with
more rounds before drawing firm conclusions.

## What to log when a case goes wrong

Which clue misled (and add it as a counterexample in `references/world/`), which tool output was wrong (file it
in the roadmap), and whether the gut call was better than the final answer (then the process overrode a good
instinct — find out why).

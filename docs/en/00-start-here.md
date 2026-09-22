# 00 · Before You Start: Learning Path and Practice Setup

[简体中文](../zh-CN/00-start-here.md) | [English](./00-start-here.md)

[Next / Bochu Systems, Software, and Files](01-bochu-systems.md)

## What you will learn

Where to start, what you can practice offline, what needs a supervised machine session, and how to fill your machine and software version card.

## Prerequisites and version scope

- You already know cutting principles, main components, and the sales context.
- Concepts are shared; concrete menus are labeled for CypCutE (manual based on software 6.4.2310) and CypCutPro (software 7.1.2432.5).
- The practice machine is not fixed yet. This guide does not bind to one machine SOP.

## Learning path

1. **Software basics (00–04)**: import → check → leads / kerf / micro joints / cooling points → nesting, sorting, simulation.
2. **Machine track (05–10)**: parts and pre-start → homing and calibration → plate and edge finding → process table and first part → pause and recovery.
3. **Independent work (11–14)**: exceptions → maintenance boundaries → three projects → demos.
4. **Migration (15)**: which Bochu concepts transfer to Raytools / Empower, and what must be relearned.

**Running case**: a double-hole plate about 80×40 mm with two Ø8 holes. Later chapters reuse this part.

```text
Offline: drawing / process prep / simulate     Supervised: power-on / calibrate / edge / beam-on
        00 ── 04                                      05 ── 10
               \                                        /
                13 projects / 14 demo prep
```

*Figure: learning path (text diagram, not a software screenshot).*

## Offline vs supervised

| Tag | Meaning |
|---|---|
| `Offline practice` | Doable without a machine, including demo mode |
| `Supervised on machine` | First time must be with a technician who knows this machine |
| `Pending machine verification` | Concept OK; buttons/values must be checked on the real version |

| Offline | Supervised on machine |
|---|---|
| Import, units, optimize, leads / kerf / micro joints / cooling points, layer mapping, nesting, sorting, software simulation | Power sequence, homing, capacitive/floating-head calibration, plate setup, edge finding, real frame/dry-run motion, beam-on trial, first-article check, breakpoint resume |

> Watching videos or finishing offline drills is not independent machine operation. Get supervision for first beam-on work.

## Fill your version card

Copy `templates/en/00-machine-version-card.md` and fill it. Keep the software name and the About-dialog runtime version separate.

| Item | Your entry |
|---|---|
| Machine model / serial | |
| Laser brand and power | |
| Cutting head model | |
| Controller (FSCUT…) | |
| Software (CypCut / CypCutE / CypCutPro / HypCut…) | |
| Runtime version from About | |
| Manual document version | |
| Software version the manual is based on | |
| Supervising technician | |

## Exercises

1. Fill a version card (runtime may be “not measured”).
2. List three offline items and three supervised items.
3. State the running-case outline and hole size in general terms (answers in ch. 13).

## Answers and criteria

1. Pass if the three version fields stay separate.
2. See the table above.
3. Outline about 80×40 mm, two holes about Ø8 (offline exercise geometry; production size follows drawing and stock).

**Criteria**: correct version split; no claim that demo mode can cut.

## Common mistakes

- Treating the manual cover version as the software runtime version.
- Believing simulation moves the machine or fires the laser.
- Clicking from someone else’s screenshot without a version card.

## Sources

- CypCutE User Manual V7.1 (based on 6.4.2310) welcome and §1.2
- CypCutPro User Manual V1.0.0 (software 7.1.2432.5) preface
- Project learning goals (not a vendor certified course)

---

[Next / Bochu Systems, Software, and Files](01-bochu-systems.md)

[简体中文](../zh-CN/00-start-here.md) | [English](./00-start-here.md)

# 15 · Migrating from Bochu to Raytools / Empower

[简体中文](../zh-CN/15-raytools-migration.md) | [English](./15-raytools-migration.md)

[Previous / Trade Shows and Customer Site Demos](14-demo-events.md)

## What you will learn

Which Bochu concepts transfer to Raytools / Empower, and which UI, licensing, and calibration steps must be relearned.

## Prerequisites and version scope

Finish Bochu chapters 03–12. Empower facts are **model × manual version** specific.

## 1. Transferable concepts

Homing, capacitive/floating-head idea, edge finding, frame, dry run, simulate, breakpoint, task, leads, kerf, micro joints, cooling points, sorting, material/layer process.

## 2. Licensing and offline (per model)

| Model / manual | Wording | Offline |
|---|---|---|
| XC3000S User Manual V1.2 | must use a dongle; without it a simulation edition opens | simulation edition |
| XC3000S Commissioning V1.4 §3.3 | 激智云 mini-program scan → machine code & dongle no. → register | — |
| XC3000Plus Commissioning V1.3 | revision log: “removed dongle as standard in 1.1” | **to verify** |

Do not write “all Empower software is dongle + simulation”. Bochu DEMO (no control card) and Empower simulation are different mechanisms.

## 3. Model matrix wording

- Use models listed on the site/catalog at read time (XC3000S / Plus / Pro / XC6000…).  
- XC7000: **no official existence evidence found in this round** (not “does not exist”).  
- CN/EN site version numbers may differ; do not rank freshness without branch proof.

## 4. Must relearn (examples)

1. Calibration entry and “reset capacitive → recalibrate”.  
2. Edge-finding parameter set.  
3. Piercing taxonomy (five levels / staged / progressive / lightning…).  
4. Advanced process (vibration, seamless micro joint, lead process).  
5. XC6000 auto-tuning, multi-task extras.  
6. Licensing/registration.  
7. Import formats.  
8. UI language and alarm area.

## 5. Concept map (example)

| Bochu | Empower (XC3000S context) |
|---|---|
| Homing | Find origin / home |
| Capacitive calibration | Capacitive sensor → one-click calibrate |
| Frame / dry run | Frame / dry run |
| Breakpoint resume | Breakpoint continue |
| Task | Machining task |
| Micro joint / cooling point | Same concepts (follow that manual’s definitions) |

Pressure calibration as in CypCutPro was not seen as a same-name standalone Empower function — `Pending machine verification`.

## Exercises

1. Five transferable concepts.
2. Can Plus reuse the S “must have dongle” sentence?
3. How should XC7000 be written?

## Answers and criteria

1. See §1.  
2. No; Plus only proves the “dongle standard removed” revision.  
3. “No official existence evidence found in this round.”

**Criteria**: per-model licensing; no absolute wording.

## Common mistakes

- One licensing story for all models.
- Presenting Chinese button glosses as confirmed English UI.

## Sources

- XC3000S User Manual V1.2 preface
- XC3000S Commissioning V1.4 §3.3
- XC3000Plus Commissioning V1.3 revision log
- Empower download center / catalog at read time

---

[Previous / Trade Shows and Customer Site Demos](14-demo-events.md)

[简体中文](../zh-CN/15-raytools-migration.md) | [English](./15-raytools-migration.md)

# 05 · From Screen to Machine: Parts and Pre-Start Checks

[简体中文](../zh-CN/05-machine-and-prestart.md) | [English](./05-machine-and-prestart.md)

[Previous / Nesting, Sorting, and Simulation](04-nesting-sorting-simulate.md) · [Next / Homing, Coordinates, and Calibration](06-homing-calibration.md)

## What you will learn

Recognize head, gas, water, exhaust, and motion zones; use a pre-start checklist. `Supervised on machine`

## Prerequisites and version scope

Chapter 04. This chapter is **parts + check principles**. Concrete power-on buttons/order are `Pending machine verification` and follow the machine SOP.  
**Do not** rewrite first-time electrical installation energizing tests as daily power-on.

## 1. Zones you must know

| Zone | Look at | Failure mode |
|---|---|---|
| Cutting head | nozzle, protective windows, ceramic, follow | dross, power loss, bad follow |
| Gas | supply gauge setting, process gas, nozzle cooling gas | burned tip, incomplete cut, burr |
| Water | level / temp / alarms | condensation, overheating |
| Exhaust | suction working, ventilation | fume hazard |
| Motion | rack, slats, travel, e-stop | head crash, plate crash |

## 2. Three “pressures” are not the same

| Concept | Where it acts | Example |
|---|---|---|
| Supply gauge setting | cylinder regulator / gauge | one M-series doc: N2 2.0 MPa, O2 0.8 MPa (**gauge setup context**) |
| Software/valve output | controller gas settings | from your process table |
| Actual pressure at nozzle | nozzle exit | CypCutPro pressure calibration maps DA valve to **nozzle** pressure (**BLT heads only**) |

Never promote a series gauge setting into universal cut pressure.

## 3. Pre-start checklist (principle)

Actions come from the machine SOP. Use `templates/en/01-prestart-checklist.md`:

1. PPE and e-stop location.  
2. Exhaust/ventilation ready.  
3. Chiller level, temperature, alarms.  
4. Gas bottle/air, leaks, gauge setting (record value + unit).  
5. Head: nozzle and window condition.  
6. Bed: slats, debris, limit switches visible.  
7. Software alarm banner clean.

`Offline practice`: write the checklist from memory. `Supervised on machine`: tick against SOP.

## 4. Running case

Before first plate: confirm stock → gas/nozzle match the process row → windows clean → exhaust on → e-stop released in the machine’s way.

## Exercises

1. Sketch five zones with one check each.
2. Explain supply gauge setting ≠ process pressure.
3. Which failures block start?

## Answers and criteria

1. See §1.  
2. Gauge is at the source; process pressure varies with material/thickness/power/nozzle.  
3. Examples: chiller alarm, gas leak, exhaust off, e-stop engaged, limit fault — per SOP.

**Criteria**: no invented button locations; installation test ≠ daily power-on.

## Common mistakes

- Using 2.0/0.8 MPa as a universal process table.
- Skipping window/nozzle condition.
- Preparing beam-on with exhaust off.

## Sources

- GWEIKE M-series connection guide (gauge adjustment context)
- GWEIKE GA installation checklist (exhaust qualitative)
- Bochu head care article
- Cutting-head manuals (model-specific)

---

[Previous / Nesting, Sorting, and Simulation](04-nesting-sorting-simulate.md) · [Next / Homing, Coordinates, and Calibration](06-homing-calibration.md)

[简体中文](../zh-CN/05-machine-and-prestart.md) | [English](./05-machine-and-prestart.md)

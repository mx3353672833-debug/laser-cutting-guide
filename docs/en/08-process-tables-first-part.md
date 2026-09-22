# 08 · Read Process Tables and Prepare the First Part

[简体中文](../zh-CN/08-process-tables-first-part.md) | [English](./08-process-tables-first-part.md)

[Previous / Plate Setup, Edge Finding, Frame, and Dry Run](07-plate-edge-dryrun.md) · [Next / First Cut and Inspection Record](09-first-cut-inspection.md)

## What you will learn

Match material, thickness, head, nozzle, and gas to a **whole process row**, and prep the first part.

## Prerequisites and version scope

Chapter 07. Values must stay conditional. The practice machine uses **its verified process sheet**. Local tables and nozzle guides are conditional references only.

## 1. Condition columns

Every row needs:

| Condition | Why |
|---|---|
| Laser model / power / fiber / optics | energy and focus |
| Material and thickness | melt and blow-away |
| Head and nozzle type/bore | symmetric jet |
| Gas | O2 exothermic / N2 speed and clean edge |
| Speed, power, pressure, focus, stand-off | surface quality together |

Quote **whole rows**. Never lift one pressure into another material.

## 2. Nozzle reference (not a hard threshold)

The GWEIKE nozzle guide lists S/D/E/B/SP and power bands, but states it is an **engineering starting reference**. Final call is the installed head and machine process table, with configuration exceptions.  
6 kW / 8 kW change-over hints are **not** exception-free rules.  
Stand-off around 0.5–1.0 mm is a reference scale only.

## 3. Gauge setting vs process pressure

N2 2.0 MPa / O2 0.8 MPa in one series installation doc is a **supply gauge setting** example — not your plate process pressure.

## 4. First-part prep sheet

1. Measured stock grade/thickness.  
2. Matching process row (head/nozzle/gas).  
3. Nozzle condition and bore.  
4. Focus policy from the row.  
5. Program: plate, inner first.  
6. Gauges: calipers, square, light.

## 5. Case table (fill on site)

| Item | On site |
|---|---|
| Material / thickness | |
| Nozzle | |
| Gas / gauge reading | |
| Row: speed/power/pressure/focus | |
| Micro joint / cooling point? | |

## Exercises

1. Why quote whole rows?
2. Are 6/8 kW nozzle tips hard rules?
3. Fill a first-part prep sheet (blanks OK).

## Answers and criteria

1. Conditions are locked together.
2. No; starting reference with exceptions.
3. Structure correct is enough.

**Criteria**: no cross-machine universal pressure/speed/power numbers.

## Common mistakes

- Copying pressure from another power sheet.
- Passing gauge setting as cut pressure.
- Ignoring nozzle model/bore.

## Sources

- GWEIKE nozzle selection guide (starting reference + exceptions)
- internal conditional table structure notes (not shipped)
- CypCutPro pressure calibration (BLT only)

---

[Previous / Plate Setup, Edge Finding, Frame, and Dry Run](07-plate-edge-dryrun.md) · [Next / First Cut and Inspection Record](09-first-cut-inspection.md)

[简体中文](../zh-CN/08-process-tables-first-part.md) | [English](./08-process-tables-first-part.md)

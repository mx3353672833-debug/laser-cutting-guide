# 07 · Plate Setup, Edge Finding, Frame, and Dry Run

[简体中文](../zh-CN/07-plate-edge-dryrun.md) | [English](./07-plate-edge-dryrun.md)

[Previous / Homing, Coordinates, and Calibration](06-homing-calibration.md) · [Next / Read Process Tables and Prepare the First Part](08-process-tables-first-part.md)

## What you will learn

Plate setup, edge finding, frame/border, dry run — and the difference between screen simulation and real motion. `Supervised on machine`

## Prerequisites and version scope

Chapter 06. CypCut tutorials Find Edge / Precheck; CypCutPro §6.2, §7.4 (tilt preferably **≤ 10°**).

## 1. Load the plate

- Flat stock on slats; avoid warped plates.
- Close guarding per machine.
- Ensure metal is under the head for follow.

## 2. Edge finding

Goal: plate angle and position so cutting can correct rotation.

1. **Home first**.  
2. Tilt preferably **not over 10°**.  
3. Wrong plate size risks **head crash** — measure and do not overshoot.  
4. Common modes: 3-point quick, 6-point for thin plate near racks, disc center-find for circles, manual 2-point angle.

## 3. Frame vs dry run

| Action | Path | Motion | Laser | Check |
|---|---|---|---|---|
| Software simulate | display | none | off | order/shape |
| Frame | rectangle / corrected box | **moves** | off (red pointer) | pointer on stock? |
| Border | outer contour | **moves** | off | envelope / obstacles |
| Dry Run | full toolpath | **moves** | off, gas off | interference |

After edge finding, frame may follow the **corrected tilted box**.

## 4. Case order

Load → home → edge find → frame (pointer on stock) → dry run → prepare beam-on.

## Exercises

1. Why home before edge finding?
2. Tilt limit?
3. Does each of simulate / frame / dry run move the machine?
4. Risk of wrong plate size?

## Answers and criteria

1. To correct machine coordinates.
2. Preferably ≤ 10°; worse accuracy otherwise.
3. Simulate no; frame and dry run **yes**.
4. Crash into rack/plate risk.

**Criteria**: three-action table correct; real motion needs supervision.

## Common mistakes

- Calling software simulate a dry run.
- Starting with the pointer off the plate.
- Guessing plate size.

## Sources

- CypCut Machining Precheck / Find Workpiece Edge
- CypCutPro §6.2 / §7.4
- running case ex01

---

[Previous / Homing, Coordinates, and Calibration](06-homing-calibration.md) · [Next / Read Process Tables and Prepare the First Part](08-process-tables-first-part.md)

[简体中文](../zh-CN/07-plate-edge-dryrun.md) | [English](./07-plate-edge-dryrun.md)

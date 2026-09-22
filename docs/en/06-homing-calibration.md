# 06 · Homing, Coordinates, and Calibration

[简体中文](../zh-CN/06-homing-calibration.md) | [English](./06-homing-calibration.md)

[Previous / From Screen to Machine: Parts and Pre-Start Checks](05-machine-and-prestart.md) · [Next / Plate Setup, Edge Finding, Frame, and Dry Run](07-plate-edge-dryrun.md)

## What you will learn

Separate homing, return-to-zero, capacitive/floating-head calibration, pressure calibration, and focus tests; know what follows the machine procedure. Mostly `Supervised on machine`

## Prerequisites and version scope

Chapter 05. CypCutPro 7.1.2432.5 §7.1–7.3; CypCutE §5.x; GWEIKE M-series FTC is a **series reference only**.

## 1. Coordinates and homing

- Machine coordinates come from machine structure/parameters; after homing they should be consistent.
- **Without homing** (CypCutPro context): alarms and often low-speed jog only until homed.
- Other alarms may block homing — clear them first.

`Supervised on machine`: real homing and direction checks.

## 2. Calibration matrix (do not merge into one cross-brand flow)

| Function | Purpose | When | Conditions |
|---|---|---|---|
| Capacitive / floating-head | sensor value vs head-plate gap | install, head/nozzle service, material change | plate under head; nozzle tight |
| Pressure calibration | DA valve voltage ↔ nozzle pressure | when pressure must be precise | **BLT heads only**; **not** redone after nozzle change |
| Focus test | relative zero focus | optic change / quality issue | per head manual |

After nozzle/ceramic change, redo **capacitive** calibration, not pressure calibration.

## 3. Example entry points (not universal)

- **CypCutPro**: capacitive calibration under CNC/calibration menus; check stability/smoothness.
- **GWEIKE M-series**: System Analysis → FTC → Floating-head Calibration (metal under head).
- **Empower XC3000S**: Capacitive sensor → one-click calibrate; reset requires recalibration.

All paths are `Pending machine verification` on your build.

## 4. Case

New nozzle before the plate: capacitive calibrate first → skip pressure calibration → frame for envelope.

## Exercises

1. Homing vs return-to-zero (concept).
2. When to redo capacitive calibration?
3. Pressure calibration after nozzle change? Why?
4. Why not reuse M-series menus everywhere?

## Answers and criteria

1. Homing builds machine coordinates; return-to-zero usually targets program/work zero (software wording).
2. Install, head/nozzle service, material change, etc.
3. No. CypCutPro says pressure calibration need not be redone after nozzle change.
4. Paths bind to software and version.

**Criteria**: capacitive vs pressure calibration separated; no invented menus.

## Common mistakes

- Only pressure calibration after nozzle change.
- Auto-cut before homing.
- Splicing cross-brand calibration steps.

## Sources

- CypCutPro §7.1–7.3
- GWEIKE M-series calibration extract
- XC3000S capacitive sensor section
- Head manuals replacement sections

---

[Previous / From Screen to Machine: Parts and Pre-Start Checks](05-machine-and-prestart.md) · [Next / Plate Setup, Edge Finding, Frame, and Dry Run](07-plate-edge-dryrun.md)

[简体中文](../zh-CN/06-homing-calibration.md) | [English](./06-homing-calibration.md)

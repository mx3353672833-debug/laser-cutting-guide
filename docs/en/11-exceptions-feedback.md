# 11 · Common Exceptions: Triage and Feedback

[简体中文](../zh-CN/11-exceptions-feedback.md) | [English](./11-exceptions-feedback.md)

[Previous / Pause, Stop, Breakpoints, and Tasks](10-pause-resume-tasks.md) · [Next / Daily Checks, Consumables, and Maintenance Boundaries](12-maintenance-boundaries.md)

## What you will learn

Capture the symptom and evidence; separate operator checks from technician work.

## Prerequisites and version scope

Chapter 10. No bypass of interlocks, no disabling protections, no forcing faulty cutting.

## 1. Two-level triage

**Operator may check first (examples)**

- Not homed → home (clear other alarms first).  
- Incomplete cut → nozzle vs thickness, speed.  
- Burr/dross → focus, power, speed, gas purity.  
- Abnormal sparks → nozzle wear; replace; do not hide with extra pressure.  
- Poor follow → capacitive/floating-head calibration first.  
- Loose nozzle fitting → pause and retighten.

**Technician / vendor (examples)**

- Height-controller parameters, bus fault codes.  
- Capacitive alarms with mechanical feedback faults.  
- Seasonal water drain/antifreeze procedures.  
- Optics, laser source, electrical installation.

## 2. Feedback form fields

Use `templates/en/03-exception-report.md`:

1. Time, machine id, runtime software version.  
2. Symptom (photo / raw alarm).  
3. Material / thickness / process row / nozzle / gas.  
4. Checks already done.  
5. Stopped? Safe to continue?

## 3. Case

Sudden hole burr on the plate: log parameters → inspect nozzle roundness/burn → focus/speed → stop and escalate with photos/alarms.

## Exercises

1. Three operator checks vs three technician cases.
2. Mini exception report (fictional sample is fine).
3. Why not “reset and go”?

## Answers and criteria

1. See §1.  
2. Fields complete.  
3. Root cause and protections unresolved.

**Criteria**: clear boundary; no hazardous advice.

## Common mistakes

- Randomly changing height-controller protection values.
- Feedback without version and process row.

## Sources

- Bochu FAQ / common problems
- CypCutPro alarms and restrictions
- head manuals collision/nozzle notes

---

[Previous / Pause, Stop, Breakpoints, and Tasks](10-pause-resume-tasks.md) · [Next / Daily Checks, Consumables, and Maintenance Boundaries](12-maintenance-boundaries.md)

[简体中文](../zh-CN/11-exceptions-feedback.md) | [English](./11-exceptions-feedback.md)

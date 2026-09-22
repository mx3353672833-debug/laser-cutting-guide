# 06 · Coordinates, homing and calibration

[简体中文](../zh-CN/06-homing-calibration.md) · [English](./06-homing-calibration.md)

Homing, setting a work zero and calibration solve different problems. Understanding the distinction explains why changing a nozzle can affect height sensing, while moving a drawing does not redefine the machine’s reference.

## Relating drawing coordinates to the machine

Machine coordinates describe machine position. Work/program coordinates place the current part. Homing establishes or corrects the configured machine reference; setting a work zero chooses a job datum. One does not replace the other.

Our plate’s lower-left corner is (0,0), with the left hole at (20,20). If the work origin is (X₀,Y₀), with no rotation or other transformation, that hole maps to (X₀+20,Y₀+20). Edge-finding angle correction adds rotation. This explains how changing the origin moves the whole part without changing its dimensions.

![Classic CypCut coordinate selection](../../assets/screenshots/bochu-cypcut/coordinates.png)

*Floating coordinate and Workpiece coordinate select coordinate modes. They are not homing commands.*

The cited CypCutE manual describes floating coordinates taking the current position as program zero when relevant checking/machining commands execute. A fixed work coordinate retains a set datum. Confirm the active mode, especially after jogging; a previously correct preview does not guarantee the next action uses the same origin.

## Different calibration functions

| Function | Relationship established or checked | Reference |
|---|---|---|
| Capacitance calibration | Sensor response versus nozzle-to-sheet distance | CypCutPro §7.2 |
| Pressure calibration | Proportional-valve control versus actual outlet pressure | Cited Pro §7.3, under its BLT conditions |
| Focus checks | Optical focus versus the process reference | Installed head instructions |

Replacing a nozzle, ceramic or related component can change sensing conditions. Perform the recalibration/following checks specified for the machine. Do not change pressure or focus settings simply because they also use the word calibration. The cited Pro manual says nozzle replacement does not require redoing its pressure calibration; that does not remove capacitance-calibration requirements.

## Check conditions and results

Before running a function, confirm that it applies to the installed equipment and that the sheet, clearance and nozzle assembly meet its requirements. Afterward, record success/failure, complete the documented result checks and verify normal following. A success message alone is not the entire check.

If calibration fails, preserve the message and conditions. Do not tune undocumented sensing settings or suppress alarms just to obtain a successful status. Resolve uncertain coordinates, head faults or unsuitable sheet conditions before edge finding.

Practice question: both holes are displaced together, but their spacing is correct. First investigate scale or location? Location and datum are the better initial lead; scale generally changes spacing too. This is an investigation clue, not a complete diagnosis.

References: CypCutE V7.1 §4.1; CypCutPro V1.0.0 §§6.1 and 7.1–7.3; [classic coordinate guide](https://www.bochu.com/tutorials/basics-machining-control/).

---

[← Understand the machine’s operating conditions](05-machine-and-prestart.md) · [Contents](README.md) · [Locate the job on the sheet →](07-plate-edge-dryrun.md)

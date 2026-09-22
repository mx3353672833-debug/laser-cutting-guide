# 10 · Resume a stopped job

[简体中文](../zh-CN/10-pause-resume-tasks.md) · [English](./10-pause-resume-tasks.md)

Resuming a job is more than pressing Start again. First establish whether the interruption changed sheet position, machine coordinates or the active task. A saved breakpoint preserves progress; it does not guarantee physical alignment.

| Interruption | Establish first | Reason |
|---|---|---|
| Normal pause, unchanged file/sheet | State permits continuation and recovery path is valid | Current-task recovery may be possible |
| Inserted urgent job | What the saved task contains and whether the original sheet remains located | A drawing file alone may not preserve job state |
| Power loss, servo fault, collision or sheet movement | Machine reference, work location and equipment condition | The breakpoint may no longer match the material |

Use your version’s definitions of Pause, Stop, Continue and breakpoint positioning. Post-stop head movement can depend on configuration; another machine’s behaviour is not a universal rule.

## Understand saved tasks

The CypCutE task function documents saving program zero, edge angle, breakpoint information and drawing for later recovery. After loading, verify material, datum and drawing state. Exporting a DXF is not equivalent to saving a task.

Practise file management offline: keep one part identifier across the geometry file, machining file and inspection record, with distinguishable revisions. Read what your task function stores and what it does not guarantee. Do not claim a successful restart without an actual controlled trial.

## A recovery decision

Both holes are complete, the outer profile is unfinished, and someone moves the sheet. The screen may still show the correct saved breakpoint, but direct continuation is inappropriate. Re-establish the relationship between program and material using the machine’s recovery procedure, then assess the remaining route.

If machine reference or post-collision condition cannot be established, remain at the inspection stage. The objective is alignment of remaining paths with the actual workpiece, not merely clearing an alarm.

References: CypCutE V7.1 §§4.8–4.9 and 5.5; CypCutPro V1.0.0 control/task sections; [Bochu saved-task recovery](https://www.bochu.com/tutorials/resume-unfinished-cutting-in-next-day/).

---

[← Cut and inspect the first part](09-first-cut-inspection.md) · [Contents](README.md) · [Investigate a cutting problem →](11-exceptions-feedback.md)

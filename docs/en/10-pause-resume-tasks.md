# 10 · Pause, Stop, Breakpoints, and Tasks

[简体中文](../zh-CN/10-pause-resume-tasks.md) | [English](./10-pause-resume-tasks.md)

[Previous / First Cut and Inspection Record](09-first-cut-inspection.md) · [Next / Common Exceptions: Triage and Feedback](11-exceptions-feedback.md)

## What you will learn

Pause / stop / breakpoint / task recovery conditions; normal interruption vs post-exception checks.

## Prerequisites and version scope

Chapter 09. CypCutPro §6.2–6.3 and task management; CypCut tutorial Resume Unfinished Cutting (*.cps).

## 1. Control actions

| Action | Meaning | Note |
|---|---|---|
| Pause | stop beam/feed (manual head/gas may be allowed) | step forward/back |
| Stop | end this run | may not return to safe point |
| Breakpoint resume | continue at stop point | has preconditions |
| Start from here | cut from a picked point | earlier path skipped |
| Save/load task | restore after job insert | zero, edge angle, breakpoint, drawing |

## 2. Breakpoint preconditions (CypCutPro context)

- Drawing not modified.  
- Process parameters unchanged.  
- No new machining run started.

If any fail, re-check instead of forcing resume.

## 3. Normal interruption vs exception

| Normal | Exception |
|---|---|
| stock change, measure, job insert | alarm, crash, incomplete cut, power loss |
| pause / task by the book | assess coordinates, nozzle, part first |

**Never** blindly reset and resume.

## 4. Case

Pause mid-part → record remaining contours → save task → insert job → load task → locate breakpoint → resume (optional re-pierce; watch the joint).

## Exercises

1. Three breakpoint preconditions?
2. What does a task file usually store?
3. Why not resume after an alarm?

## Answers and criteria

1. No draw edit, no param change, no new run.  
2. Zero, edge angle, breakpoint, drawing, etc.  
3. Coordinates/part/consumables may have changed.

**Criteria**: all preconditions; no “always resumable”.

## Common mistakes

- Resuming after changing parameters.
- Treating screen simulate as breakpoint evidence.

## Sources

- CypCutPro machining control / task management
- CypCut Resume Unfinished Cutting

---

[Previous / First Cut and Inspection Record](09-first-cut-inspection.md) · [Next / Common Exceptions: Triage and Feedback](11-exceptions-feedback.md)

[简体中文](../zh-CN/10-pause-resume-tasks.md) | [English](./10-pause-resume-tasks.md)

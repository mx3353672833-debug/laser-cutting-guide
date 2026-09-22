# 11 · Investigate a cutting problem

[简体中文](../zh-CN/11-exceptions-feedback.md) · [English](./11-exceptions-feedback.md)

“It cuts badly” is not a sufficiently specific fault report. First distinguish file problems, positioning/motion problems and cut-quality problems. Change one justified condition at a time so that the result remains interpretable.

Record the part identifier, full software version, exact alarm/code, stage of the job, recent changes and whether the sheet moved. Label part orientation and defect locations in photographs. Preserve the current file and recipe before recovery or adjustment.

| Symptom | First checks | Avoid |
|---|---|---|
| Fixed scale error after import | Units, measurement reference and importer behaviour | Using kerf compensation to fix scale |
| Repeated profile travel | Duplicate geometry/imports, target layers and order | Hiding extra time by increasing speed |
| Whole part displaced | Zero, coordinate mode and sheet location | Editing design dimensions first |
| Local incomplete cut | Recipe match, supply, nozzle and path location | Changing speed, focus and pressure together |
| Abnormal following/collision risk | Stop motion, preserve the message, inspect sheet/head state | Repeated reset or bypassing protection |

Start with facts that do not change machine configuration: file identity, material, nozzle specification and the alarm text. Electrical, optical, motion-configuration and interlock work belongs with the relevant qualified technician.

## Write a useful report

“After hole 2, continuous dross along the right outer edge. Same material batch; nozzle replaced today. File P01-r03, recipe SS-…, photo orientation marked. Focus and pressure not changed.” This is more useful than guessing that nitrogen is the problem: it preserves the symptom, recent change and current state.

Use the [fault report](../../templates/en/03-exception-report.md). You need accurate observations, not a premature diagnosis. Online symptom tables suggest checks; they do not diagnose your machine.

Exercise: pressure, speed and focus were changed together and the edge improved. Does that prove pressure was responsible? No. Preserve a baseline and use approved, recorded, small-step trials to distinguish effects.

References: matching controller alarm instructions; [Bochu cutting problem analysis](https://www.bochu.com/pro_information/激光切割常见问题分析及解答/).

---

[← Resume a stopped job](10-pause-resume-tasks.md) · [Contents](README.md) · [Inspect consumables and record maintenance →](12-maintenance-boundaries.md)

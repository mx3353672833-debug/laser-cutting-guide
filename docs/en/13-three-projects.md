# 13 · Three practical projects

[简体中文](../zh-CN/13-three-projects.md) · [English](./13-three-projects.md)

These projects connect the earlier functions. Produce a saved, reopenable offline result first; add actual recipe and inspection records when machine work is available. Keep each job’s files and checks together.

## Project A: deliver a two-hole plate file

[Download ex01](../../exercises/dxf/ex01-double-hole-plate.dxf).

Load one copy into an empty document. Verify 80 × 40 mm overall, two Ø8 holes and 40 mm centre spacing. Exclude annotation. Check that leads enter each hole and the outer profile from waste. Understand compensation using Chapter 3; without a machine-specific kerf basis, do not label an exercise setting production-ready. Sequence both holes before the outside, simulate and check for annotation or duplicate paths. Save, close, reopen and check again.

Deliver the machining file, a simulation note and an inspection plan. Record observations such as “long edge 80; hole diameter 8; both holes precede outer profile; annotation excluded,” rather than simply “done.”

<details><summary>Project A reference</summary>

One outer profile, two circles centred at (20,20)/(60,20), radius 4. Micro joints can split the path, so do not require exactly three segments. A physical first part needs overall dimensions, hole diameters and spacing checked against the drawing’s tolerances.

</details>

## Project B: separate annotation from intended marking

[Download ex07](../../exercises/dxf/ex07-layer-process.dxf).

The outline is 70 × 35 mm with one radius-5 hole. MARK contains two short lines and P-01 text; TEXT0 contains annotation. Select each group and identify its source layer.

Create two copies. B1 machines only the outer profile and hole; MARK/TEXT0 are excluded. B2 prepares intended marking geometry, enabling a marking process only when a suitable recipe and text handling are available. Annotation remains excluded. Without a validated marking process, deliver a mapping plan marked pending rather than substituting cutting settings.

Deliver a source-layer → target-layer → purpose table. Check B1 playback excludes text and B2 matches the intended behaviour. If text does not import, inspect text support and outline conversion before diagnosing a software fault.

<details><summary>Project B reference</summary>

Source names identify objects; target settings determine machining behaviour. Changing MARK’s colour or placing TEXT0 last does not establish that the required process is configured.

</details>

## Project C: hand over a three-part layout

[Download ex08](../../exercises/dxf/ex08-multi-part-layout.dxf).

Confirm three 50 × 40 mm parts, each with one Ø12 hole, inside a 190 × 75 mm reference sheet. Exclude SHEET/NOTE. Check nominal spacing, then check actual path extents after leads and compensation. Retain hole-before-outside order for each part. Compare part-by-part completion with alternative inner-profile ordering without enabling fly cutting or common-line cutting for this exercise.

Deliver the file, preview, coordinate/sheet notes and a short handover. Another reader should be able to identify part count, holes per part, reference-frame exclusion and remaining machine-specific checks without asking you to reconstruct the job.

<details><summary>Project C reference</summary>

Three single-hole rectangles. Sheet extents: x=5–195, y=5–80. Part x ranges: 10–60, 75–125, 140–190; y=15–55. Nominal margins are 5 mm left/right, 10 bottom and 25 top. These are drawing values; leads and compensation can require additional space.

</details>

## Isolate a problem before combining tasks

Use [ex02](../../exercises/dxf/ex02-wrong-units.dxf) for units, [ex04](../../exercises/dxf/ex04-open-contour.dxf) for closure, [ex03](../../exercises/dxf/ex03-duplicate-lines.dxf) for duplicates, [ex05](../../exercises/dxf/ex05-tiny-entities.dxf) for tiny geometry and [ex06](../../exercises/dxf/ex06-nested-contours.dxf) for nested profiles. One deliberate defect at a time is easier to understand than repeated trial edits on production files.

References: original DXFs and [exercise answers](../../exercises/README.en.md); software sources in Chapters 2–4.

---

[← Inspect consumables and record maintenance](12-maintenance-boundaries.md) · [Contents](README.md) · [Prepare a repeatable demonstration →](14-demo-events.md)

# 03 · Put the toolpath in the right place

[简体中文](../zh-CN/03-leads-kerf-microjoints.md) · [English](./03-leads-kerf-microjoints.md)

With the drawing checked, decide what will be machined, where cutting enters each profile, and which side receives the toolpath offset. Continue with the saved two-hole plate.

## Exclude annotation from cutting

In ex01, CUT contains the rectangle and holes; MARK contains a text label. These are DXF source-layer names. MARK does not automatically mean marking or non-machining.

Use the matching version’s DXF layer mapping to assign CUT to the intended machining layer. Assign annotation to a non-machining layer, or explicitly exclude it from the working copy. Check the target-layer settings: changing display colour alone is not proof of a process assignment.

![Classic CypCut layer settings](../../assets/screenshots/bochu-cypcut/layer-cut.png)

*This official image identifies the settings window. Its speed, power and pressure values are not a recipe for this exercise.*

In [ex07](../../exercises/dxf/ex07-layer-process.dxf), a P-01 mark would need an appropriate marking process if it is intended on the part. Text used only as annotation stays out of machining. Check whether your version imports text directly or requires outline conversion.

## Place the pierce point in waste

Piercing establishes a cut through solid sheet. Its local heating and spatter differ from steady cutting. Starting directly on the finished edge may leave a defect there. A lead-in starts in waste and joins the required contour.

![Retained material determines lead direction](../../assets/screenshots/bochu-cypcut/inner-outer.png)

*In the left example, material outside the circle remains, so the lead enters from inside. In the right example, the circular part remains, so the lead enters from outside.*

Select each hole and add a lead, checking that its pierce point lies inside the circle. Select the outer rectangle and place its start outside the part. Zoom in and make sure leads do not cross nearby retained profiles. Automatic placement still needs inspection.

In offline practice, compare positions and directions using a clearly identified exercise copy. Production lead length depends on material thickness and piercing conditions. A software default is not an approved process value.

## Compensation moves the toolpath

Take a geometry-only example: nominal width 80 mm and an assumed kerf width of 0.20 mm. Following the nominal boundary removes half a kerf from each side, leaving about 79.80 mm. Moving each side of the toolpath outward by 0.10 mm places the ideal cut edges back on the drawing boundary.

Under the same ideal model, following an 8 mm circle makes an opening of about 8.20 mm; its path needs to move inward. The assumed 0.20 mm is an explanation, not a recommended kerf value.

![Outer-profile offset geometry](../../assets/figures/en/fig-06-kerf.svg)

Check whether your compensation dialog asks for kerf width or offset distance. Enter the quantity it actually requests. Do not halve the input merely because the physical offset is half the kerf. Production values should come from measured cutting results.

Inspect the resulting path: outside the rectangle, inside the holes. Also check that compensation has not already been applied in CAD. Scaling the entire drawing changes hole spacing and cannot replace kerf compensation.

## A micro joint retains material; a cooling point adds a pause

A fully separated part can tip or lose support. A conventional micro joint leaves a short material connection. A cooling point turns the beam off and applies the configured blowing delay before continuing, addressing local heat accumulation.

| Feature | Intended result | What to inspect |
|---|---|---|
| Conventional micro joint | A small material connection remains | Position relative to mating edges; suitable length |
| Cooling point | Cutting continues around the complete contour | Actual need for corner cooling and a justified delay |
| Seamless micro joint | A controlled remaining root assists removal | The relevant Pro function and root settings; not necessarily beam-off |

In an exercise copy, add one conventional joint on a non-mating straight edge of the outer profile. Inspect the mark, remove it and compare the path. Demonstrate a cooling-point mark separately. You do not need every optional feature on the first plate. Joints on hole slugs depend on support and the job; “never use them on holes” is not a universal rule.

## Save a result you can inspect

Keep a clean-geometry copy and a separate prepared machining copy. Reopen the latter and check annotation exclusion, lead placement, compensation direction and joint marks.

<details>
<summary>If the outside is undersize and the holes oversize, should you enlarge the drawing?</summary>

Not as a general correction. Scaling changes designed hole spacing and cannot address opposite inside/outside errors. First establish correct imported dimensions, then check compensation, direction and the measured kerf basis.

</details>

References: CypCutE V7.1 §§3.1–3.4 and 3.16; CypCutPro V1.0.0 §§3.3–3.4 and table 5-2; [official process tutorial](https://www.bochu.com/tutorials/basics-technique-setting/).

---

[← Clean and check the drawing](02-import-drawings.md) · [Contents](README.md) · [Plan the cutting sequence →](04-nesting-sorting-simulate.md)

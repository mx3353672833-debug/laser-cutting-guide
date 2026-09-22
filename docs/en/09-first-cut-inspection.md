# 09 · Cut and inspect the first part

[简体中文](../zh-CN/09-first-cut-inspection.md) · [English](./09-first-cut-inspection.md)

A first part checks the combined result of file preparation, machine condition, recipe and actual material. Start with a small trial and inspect it before committing a full sheet.

## Confirm the checked job is still the active job

Verify filename, material, target layers, recipe and zero. Confirm that neither the sheet nor program changed after placement and path checks. Start according to the machine procedure and observe through the permitted means. Use the specified stop response for abnormalities; do not reach into the motion area to adjust material.

Before removal, follow the machine’s safe-state and hot-part handling procedure. If the part remains attached, distinguish planned micro joints from unintended incomplete cutting. Forcing it free can hide the defect.

## Inspect the plate

Measure both overall dimensions and both hole diameters. Check centre spacing using the drawing’s required inspection method. Calipers do not directly grip a hole centre: the inner gap between equal holes is not the centre distance. The method and its uncertainty must suit the inspection requirement.

| Observation | Record first | Investigation direction |
|---|---|---|
| Outside undersize, holes oversize | Actual external and hole measurements | Imported size, compensation and kerf basis |
| Local roughness on one side/corner | Location and cutting direction | Local path, support, process and head condition |
| Dross or incomplete cutting | Material, location and whether local/continuous | Recipe match, gas supply and nozzle condition |
| Part distortion | Location and support arrangement | Heat, sequence and support |

These organise investigation; none alone proves a single parameter caused the problem.

## A worked inspection decision

This is a fictional measurement exercise. If a drawing specifies 80.00 ± 0.10 mm and the part measures 79.70 mm, that dimension fails. A shiny surface does not change the result. Without a specified tolerance, record the measurement rather than inventing an acceptance limit.

Keep the recipe revision and photo locations with the result. “Dross on the underside of the right-hand edge, photo B” is more useful than “poor quality.” Use the [inspection record](../../templates/en/02-first-article-inspection.md) for release status, reviewer and next action.

<details>
<summary>Does a micro-jointed part remaining attached necessarily indicate incomplete cutting?</summary>

No. Check whether connections match the intended joint locations and whether the remaining profiles are complete. Attachment elsewhere needs investigation.

</details>

References: CypCutPro V1.0.0 §§3.3–3.4; [Bochu cutting problem analysis](https://www.bochu.com/pro_information/激光切割常见问题分析及解答/). Drawing and local inspection requirements determine acceptance.

---

[← Read a cutting recipe](08-process-tables-first-part.md) · [Contents](README.md) · [Resume a stopped job →](10-pause-resume-tasks.md)

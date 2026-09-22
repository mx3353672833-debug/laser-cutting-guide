# 08 · Read a cutting recipe

[简体中文](../zh-CN/08-process-tables-first-part.md) · [English](./08-process-tables-first-part.md)

When someone gives you a process table, first identify the equipment, material and thickness it applies to. Then read speed, pressure and focus. An isolated speed value does not describe a usable recipe.

## Establish the conditions behind the row

| Condition | Why it matters |
|---|---|
| Material and thickness | Identifies the relevant process family |
| Laser, power and optical configuration | Equal nominal power does not guarantee equal optical conditions |
| Head, nozzle family and aperture | Determines mechanical and gas-flow compatibility |
| Gas and supply conditions | Different gases are not interchangeable based on pressure alone |
| Piercing versus cutting stage | Height, power and timing may differ between stages |

Once those conditions match, read speed, power, pressure, focus and height with their units. Pay attention to m/min versus mm/s and bar versus MPa: 1 MPa = 10 bar; 1 m/min is about 16.67 mm/s.

## Pressure at different locations

A supply gauge describes upstream supply conditions. Software process pressure is a machining setting. Actual nozzle pressure also depends on the gas circuit and control relationship. The M-series example of nitrogen 2.0 MPa and oxygen 0.8 MPa describes supply-gauge settings in that documentation; it is not a recipe for your plate.

Focus signs also depend on the head and software definition. Copying an F value without its datum and sign convention can change its meaning.

## Practise with an incomplete recipe

Suppose a row says only “2 mm stainless, nitrogen, speed …” and omits head, nozzle, laser power and provenance. It helps identify questions, but is not a complete first-part recipe. Obtain the missing conditions and a matching builder-supplied or locally validated process before preparing the machining copy.

A nozzle guide is also a conditional reference. Do not choose solely from a universal 6 kW or 8 kW threshold; the manufacturer’s guide includes configuration exceptions.

## Make the setup reproducible

In the [first-part record](../../templates/en/02-first-article-inspection.md), identify material, thickness, machine, nozzle, gas, recipe source and units. Record which row was used and what changed. Mark missing values as unavailable rather than filling them with software defaults.

Question: can two nominally 6 kW machines share a recipe automatically? No. Compare the conditions above and establish applicability. This chapter deliberately provides no cross-machine cutting recipe.

References: [GWEIKE nozzle reference and exceptions](https://www.gwklaser.com/fiber-laser-cutting-nozzle-selection-guide.html); CypCutPro V1.0.0 Chapter 5 and §7.3; reviewed process-table field structure.

---

[← Locate the job on the sheet](07-plate-edge-dryrun.md) · [Contents](README.md) · [Cut and inspect the first part →](09-first-cut-inspection.md)

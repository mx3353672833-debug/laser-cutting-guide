# 15 · Transfer your skills to RayTools

[简体中文](../zh-CN/15-raytools-migration.md) · [English](./15-raytools-migration.md)

Bochu practice teaches transferable skills: checking geometry, identifying retained material, placing leads, planning sequence and inspecting results. In RayTools/Empower, you need to learn how the particular software expresses those actions and how the installed machine responds.

## Transfer the same part first

Keep ex01 as the test case. Identify the XC controller and software version, then repeat import, measurement, mapping, leads and simulation. Compare the same dimensions and path outcomes rather than searching for controls in Bochu-like positions.

| Concept you already know | Reconfirm in the new system |
|---|---|
| Drawing and machining path differ | Geometry, process and saved-task formats |
| Source layers need target behaviour | Default mapping, first/last processing and exclusions |
| Compensation moves towards waste | Input quantity, sign convention and display |
| Recovery depends on position | Task storage, breakpoint positioning and continuation conditions |
| Following and edge finding need machine readiness | Calibration entry points, strategies and alarms |

## Licensing is model-specific

The XC3000S user manual V1.2 describes a dongle and a simulation version without it. Its commissioning manual V1.4 §3.3 documents cloud registration. XC3000Plus commissioning manual V1.3 only records removal of the dongle from standard equipment; that does not establish the complete new licensing mechanism or equivalence with S.

For XC7000, this research found no official existence evidence. That is a search limitation, not proof that the model cannot exist. Use the actual model on the equipment and screen when choosing documentation.

## A practical transfer exercise

Record the Bochu entry point and the corresponding RayTools entry point in two columns. After each step, record the same result: 80 × 40, two Ø8 holes, annotation excluded, holes before outside. Calibration, piercing settings and task recovery require confirmation against the new system and machine; matching labels do not justify copying parameters.

If only simulation is available or licensing is incomplete, finish the supported file exercises and retain real-control tests as unresolved items. Understanding the process speeds up learning a second system, but does not replace experience with the unfamiliar machine.

References: [official download centre](https://www.empower.cn/download-2/); XC3000S user V1.2 and commissioning V1.4 manuals; XC3000Plus commissioning manual V1.3.

---

[← Prepare a repeatable demonstration](14-demo-events.md) · [Contents](README.md)

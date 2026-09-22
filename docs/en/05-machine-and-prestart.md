# 05 · Understand the machine’s operating conditions

[简体中文](../zh-CN/05-machine-and-prestart.md) · [English](./05-machine-and-prestart.md)

On the computer, a mistake often appears as incorrect geometry or a bad path. At the machine, the same file also depends on sheet support, head condition, gas, cooling and guarding. Start by understanding what the cutting head needs rather than memorising switches from another machine.

## Follow the supporting systems

The optics focus the beam, the nozzle directs assist gas, and the ceramic/sensing assembly contributes to height detection. Sheet height can vary, so following requires a valid calibration relationship. Protective-window locations and specifications belong to the particular head; another machine’s spare-part dimensions are not a substitute.

Cooling circuits serve the laser or optical components. Extraction handles cutting fumes. Gas supply must provide the identified gas under the required supply conditions. The bed supports the sheet. Software settings rely on these physical conditions being present.

| Observation | What it affects | First check |
|---|---|---|
| Damaged nozzle opening | Gas flow and head condition | Installed nozzle specification and head inspection procedure |
| Poorly supported or raised sheet | Following and travel clearance | Loading and support requirements |
| Uncertain or insufficient gas | Whether recipe conditions are met | Gas identification, supply state and recipe |
| Cooling or extraction problem | Readiness to operate | Equipment status and machine procedure |

These are investigation starting points, not one-to-one fault diagnoses.

## Use the machine’s startup sequence

The builder determines how mains power, cooling, laser, drives and auxiliaries are coordinated. Some actions use cabinet controls; others are handled by software or PLC logic. An installation power-on test is not a daily startup procedure.

Locate the machine’s operating instructions and verify the expected ready state after each action. A clear software alarm bar does not establish that extraction is effective or that the sheet is supported.

## Complete one prestart check

Use the [prestart record](../../templates/en/01-prestart-checklist.md) to identify the machine, software, material, nozzle and recipe. Confirm the work area is clear, guarding/interlocks operate correctly, stopping controls are understood, and cooling, gas and extraction meet this machine’s requirements.

Understand axis directions and travel areas before performing homing or other motion. Do not fire the laser merely to see whether the machine responds. Resolve an unfamiliar step through the machine instructions or a demonstration by someone competent with that equipment.

You have completed this chapter when you can explain the purpose of each check. Confirming gas identity, for example, establishes a recipe condition rather than merely filling a box.

References: [GWEIKE installation requirements](https://www.gwklaser.com/about/technical/fiber-laser-cutter-installation-requirements-checklist.html) and the installed head/laser instructions. Startup order remains machine-specific.

---

[← Plan the cutting sequence](04-nesting-sorting-simulate.md) · [Contents](README.md) · [Coordinates, homing and calibration →](06-homing-calibration.md)

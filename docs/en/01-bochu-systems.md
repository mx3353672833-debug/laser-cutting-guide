# 01 · Find your software and workspace

[简体中文](../zh-CN/01-bochu-systems.md) · [English](./01-bochu-systems.md)

Start with the software title and its About page. Record the product name and full running version. Bochu is the manufacturer, FSCUT identifies a controller family, and CypCut, CypCutE, CypCutPro and HypCut are different software products. Machine power alone does not identify the software.

## Choose the matching reference

| Product | Reference used here | How to use it |
|---|---|---|
| Classic CypCut | Bochu’s English introductory tutorials | Recognise functions in the screenshots |
| CypCutE | Document V7.1, based on software 6.4.2310 | Check E-specific menus and instructions |
| New-interface CypCutPro | Document V1.0.0, software 7.1.2432.5 | Check Pro control and calibration instructions |

Document V7.1 does not mean the installed software is version 7.1. Record the running version separately from the manual’s version and software baseline. See [version scope](version-scope.md) for other branches.

## Practise on a design computer

Use the [official download centre](https://www.bochu.com/ch/soft/) and the version confirmed for the intended machine. Do not replace production software just to match a tutorial. Offline drawing practice does not require changing machine-axis, laser or gas configuration.

The E and Pro manuals used here describe demonstration mode on a computer without a control card. It supports preparation, not actual machining control. Classic CypCut documentation has different dongle-related wording; do not generalise it across products. Confirm the current mode before practising. If startup is blocked, record the exact message and version and resolve the branch-specific requirement.

## Recognise three working areas

![Classic CypCut machining console](../../assets/screenshots/bochu-cypcut/control-panel.png)

*Bochu’s classic CypCut illustration. The red outline locates the machining console at the lower right. The large black area is the drawing board. This is not a screenshot of our own E/Pro session.*

Selecting a drawing object, editing its process and moving the cutting head are different operations. The first two normally use the drawing board and process tools; many controls in the machining console command real hardware.

![Graphic process tools](../../assets/screenshots/bochu-cypcut/technique-panel.png)

*The highlighted toolbar contains Lead, Compensate, Micro Joint and Cooling Point. We will use these functions in Chapter 3.*

| Area | Locate first | Purpose |
|---|---|---|
| File menu | Open, Import, Save As | Load, append and save a working copy |
| Drawing/process tools | Select, measure, leads, compensation | Prepare geometry and paths |
| Machining console | Simulate, Start, Pause, Stop | Distinguish screen playback from machine execution |

Start is not a preview command. Use the documented simulation function for screen playback. Recognise gas, laser, following, jog and homing controls without clicking through them to learn what they do.

## Open versus Import

Open switches to a file. Import adds geometry to the current drawing board. Importing the same file twice can leave coincident copies that still look like a single part.

Begin ex01 in an empty document. Use Import later when you intentionally add more parts. Save a working copy, close it and reopen it to confirm that the edits were retained.

A DXF exchanges geometry. Leads, sequence and machining settings need the software’s machining-file format. Exporting another DXF is not proof that the complete process has been saved. The [official format guide](https://www.bochu.com/tutorials/basics-import-drawing/) distinguishes geometry, toolpath and nesting-package files.

## Before continuing

Record the product and running version, then locate Open, Import, a measurement tool and simulation. If the screen differs, use the matching manual. Next, we will inspect the actual plate geometry.

References: CypCutE V7.1 welcome page and §§1.3–1.4; CypCutPro V1.0.0 preface; [Bochu machining controls](https://www.bochu.com/tutorials/basics-machining-control/).

---

[← Start with one drawing](00-start-here.md) · [Contents](README.md) · [Clean and check the drawing →](02-import-drawings.md)

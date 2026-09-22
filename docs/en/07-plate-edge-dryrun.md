# 07 · Locate the job on the sheet

[简体中文](../zh-CN/07-plate-edge-dryrun.md) · [English](./07-plate-edge-dryrun.md)

A nesting layout inside a screen border still needs locating on the real sheet. Establish sheet condition, coordinates and the starting position before edge finding and travel checks.

## Edge finding establishes position and rotation

If a sheet is rotated slightly, placing a zero at one corner does not describe its far end. Edge finding uses sheet-edge information to determine location and angle. It does not correct drawing dimensions or validate a cutting recipe.

![Classic CypCut edge-finding entry](../../assets/screenshots/bochu-cypcut/find-edge.png)

*The official example highlights Find Edge on the CNC tab. Use the relevant E/Pro manual for those products.*

## Match sheet dimensions to machine axes

![Classic edge-finding settings](../../assets/screenshots/bochu-cypcut/find-edge-steps.png)

*Inspect sheet X/Y dimensions, strategy and start point. The pictured numbers belong to the original example.*

Sheet X is the length along the machine’s X axis; Y follows its Y axis. These do not necessarily match what looks like the long and short edges from where you stand. The cited E manual recommends setting dimensions slightly smaller than the actual sheet being found, while still matching the sheet and strategy; this is not permission to choose arbitrary smaller dimensions.

Follow the machine’s homing requirements, confirm normal following and start over actual sheet material. The cited manual specifies sheet inclination no greater than 10°. Do not replace that with a vague approximation. Resolve uncertain size, strategy or start position before executing motion.

## Inspect placement after finding edges

Check that the reported datum and angle make sense for the physical sheet. Preview the complete job inside usable material. If nesting already includes a margin, check how the edge-finding margin interacts with it. Clamps and damaged edges also reduce usable space.

Perform frame and dry-run checks according to the machine procedure. Establish path clearance and head-height conditions before motion; a dry run is a verification step, not a collision probe. Moving the sheet, changing zero or editing the layout invalidates the checks affected by that change.

Exercise: sketch a rotated sheet with X/Y axes, a start point, a layout boundary and a clamp. Explain why a bounding frame inside the sheet is insufficient. An internal clamp or raised material can still obstruct the route, and a frame move does not traverse every internal path.

References: CypCutE V7.1 §5.2; CypCutPro V1.0.0 §7.4; [Bochu edge-finding guide](https://www.bochu.com/tutorials/find-sheet-edge-and-rotation-angle/).

---

[← Coordinates, homing and calibration](06-homing-calibration.md) · [Contents](README.md) · [Read a cutting recipe →](08-process-tables-first-part.md)

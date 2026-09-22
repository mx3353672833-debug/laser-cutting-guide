# 00 What the job actually is

[简体中文](../../zh-CN/learn/00-why-this-works.md) | [English](./00-why-this-works.md)

For people who have never opened cutting software. Read this first.

## One line

Fix the drawing and the order on the PC. Find the plate and dry-run on the machine. Cut one part. Measure.  
Numbers always belong to this stock + this machine + this process row. Copy the row. Do not invent.

## Six steps

![Official flow](../../../assets/screenshots/bochu-cypcut/flow-overview.png)

That image is Bochu’s official overview. Walk it on your software:

| Step | Do | Skip and |
|---|---|---|
| Import | get the shape in | nothing to cut |
| Optimize | measure, close gaps, dedupe | wrong size, double cuts |
| Technique | lead, kerf, micro joint, cooling point | burns, wrong size, flying parts |
| Toolpath | holes first, outer last | part drops early |
| Precheck | simulate / frame / dry run | crash or cut off sheet |
| Control | start, pause, breakpoint | — |

Simulate, dry run, cut are not the same:

- Simulate: machine stays put. No laser. Screen only.
- Frame / dry run: machine moves. No laser. Check range and crashes.
- Cut: moves, laser on.

## Lead, kerf, micro joint, cooling point

All four exist because the beam makes a mess.

![Lead](../../../assets/screenshots/bochu-cypcut/lead-line.png)

Lead: starting on the part edge burns a scar. Pierce in scrap, then walk onto the contour. You get a short entry tail.

![Kerf](../../../assets/screenshots/bochu-cypcut/kerf-comp.png)

Kerf: the beam removes a slit. Without offset, outer shrinks and holes grow. Shift the path about half a kerf. Measure kerf yourself.

![Micro joint](../../../assets/screenshots/bochu-cypcut/micro-joint.png)

Micro joint: cut-through parts tip up and hit the head. Leave a tiny uncut link so the part hangs on the skeleton. Snap it off later.

![Cooling point](../../../assets/screenshots/bochu-cypcut/cooling-point.png)

Cooling point: corners cook. Dwell, laser off, blow gas, continue.

Micro joint stops tipping. Cooling point stops corner burn. Gaps on the path are joints. Solid dots are cooling points.

## Practice part

Everything later uses this 80×40 plate with two holes.

```text
┌──────────────┐
│  ○        ○  │
│              │
└──────────────┘
```

File: [ex01-double-hole-plate.dxf](../../../exercises/dxf/ex01-double-hole-plate.dxf)

No machine yet is fine. Demo mode can do the six steps.

## Working alone

PC work is all yours. Before touching a live machine, memorize lesson 05’s six lines: e-stop, guard, exhaust, alarms. If you are unsure, stop. Do not poke buttons.

## Order

00 here → [01 UI](01-ui-tour.md) → [02 Import](02-first-import.md) → [03 Technique](03-first-technique.md) → [04 Precheck](04-first-precheck.md) → [05 Machine](05-first-on-machine.md)

Stuck: [stuck guide](00-stuck.md)

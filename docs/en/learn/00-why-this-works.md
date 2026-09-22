# 00 · Why this works (the story first)

[简体中文](../../zh-CN/learn/00-why-this-works.md) | [English](./00-why-this-works.md)

> **For absolute beginners.** Readable on a phone. After this page you should be able to say what you are actually doing on the PC.

---

## One sentence

> On the PC: shape → cut order → entry point → kerf offset → keep small parts from flying.  
> Then on the machine: find the plate → dry-run the range → cut the first part → measure.  
> **Every number is tied to this stock, this machine, this process row.**

---

## The 6-step map (official overview)

![CypCut operation flow (official)](../../../assets/screenshots/bochu-cypcut/flow-overview.png)

*Figure · Source: Bochu official tutorial “Operation Flow”.*

| Step | What you do | Skip it and… |
|---|---|---|
| 1 Import drawing | Put the shape in | nothing to cut |
| 2 Optimize drawing | Check size, close gaps, dedupe | wrong size / double cuts |
| 3 Technique setting | Lead, kerf, micro joint, cooling point | burn marks, wrong size, tipped parts |
| 4 Toolpath planning | Inner first, outer last | part drops early, crash risk |
| 5 Machining precheck | Simulate / frame / dry run | crash or cut off the sheet |
| 6 Machining control | Start / pause / breakpoint | — |

**Simulate ≠ dry run ≠ beam-on** (the #1 beginner mix-up):

| | Machine moves? | Laser on? | Use |
|---|---|---|---|
| Software simulate | no | no | see path/order on screen |
| Frame / dry run | **yes** | no | real envelope / collisions |
| Cut | yes | **yes** | make the part |

---

## Why lead / kerf / micro joint / cooling point

They cancel physical side effects — not software being fussy.

![Lead line (official UI)](../../../assets/screenshots/bochu-cypcut/lead-line.png)

**1. Lead line** — Starting on the part edge burns a scar. Pierce in **scrap**, then walk onto the contour.

![Kerf compensation (official UI)](../../../assets/screenshots/bochu-cypcut/kerf-comp.png)

**2. Kerf compensation** — The beam removes a slit. Without offset: outer size undersizes, holes oversize. Offset ≈ half kerf. Measure kerf on a real cut.

![Micro joint (official UI)](../../../assets/screenshots/bochu-cypcut/micro-joint.png)

**3. Micro joint** — Cut-through parts tip up and can hit the head. Leave a tiny **uncut link** so the part stays on the skeleton.

![Cooling point (official UI)](../../../assets/screenshots/bochu-cypcut/cooling-point.png)

**4. Cooling point** — **Not** a micro joint. At a sharp corner, dwell, turn laser off, blow gas to cool, then continue.

> **Memory hook**: micro joint = stop tipping/crash; cooling point = stop corner burn.

---

## Running part: 80×40 double-hole plate

![ex01](../../../assets/previews/en/ex01-double-hole-plate.png)

Download: [ex01-double-hole-plate.dxf](../../../exercises/dxf/ex01-double-hole-plate.dxf)

You do not need a machine yet. Finish the 6 software steps first.

---

## What you can do with no teacher

| Yes | Notes |
|---|---|
| Learn the UI | next lesson |
| Install demo mode | no control card still designs |
| Import and measure DXF | fully offline |
| Set lead/kerf/micro joint/cooling point + simulate | fully offline |
| Memorize machine safety list | before first beam-on |

**Safety floor** (for when you go alone): know the e-stop; do not fire with guards open; do not force-run past alarms. These are **rules you follow**, not a forever babysitter.

---

## Path

1. This page  
2. [01 UI tour](01-ui-tour.md)  
3. [02 First import](02-first-import.md)  
4. [03 First technique](03-first-technique.md)  
5. [04 First precheck](04-first-precheck.md)  
6. [05 First on-machine](05-first-on-machine.md)  
7. Stuck? [00-stuck](00-stuck.md)

Next: [01 UI tour](01-ui-tour.md)

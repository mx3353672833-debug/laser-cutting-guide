# 00 · Start with one drawing

[简体中文](../zh-CN/00-start-here.md) · [English](./00-start-here.md)

A customer gives you a drawing and asks for a sample. Before you can hand over a part, you need to establish that the drawing is correct, decide how the machine will travel, and make sure the job can be cut on the sheet in front of you.

We will work through those decisions using one small mounting plate: 80 × 40 mm, with two 8 mm diameter holes on 40 mm centres. Its simple geometry makes mistakes easier to locate.

![The running example, with overall dimensions, hole diameters and spacing](../../assets/figures/en/workpiece.svg)

[Download the DXF](../../exercises/dxf/ex01-double-hole-plate.dxf) · [Exercise notes](../../exercises/answers/en/ex01-double-hole-plate.md)

## A drawing is not yet a cutting program

The DXF describes a rectangle and two circles. It does not decide where to pierce, which hole to cut first, which side receives the kerf offset, or which material recipe suits your machine.

Consider kerf compensation. A cut has width. If the beam centre follows the rectangle’s nominal edge, it removes material on both sides of that edge, so the retained part may be undersize. The outside toolpath must move towards the surrounding waste. At a hole, the retained material is outside the circle, so the toolpath moves into the hole instead.

Sequence matters too. Cutting the outside profile first can leave the part poorly supported before the holes are finished. Our starting sequence is therefore both holes followed by the outside profile. The drawing and the path used to cut it are related, but they are not the same thing.

## Build a file you can explain

Chapters 1–4 can be practised on a design computer disconnected from the machine. Each chapter uses the same plate.

| Chapter | What you produce | What you should be able to explain |
|---|---|---|
| 1 | Software name and running version | Whether you are using CypCut, E or Pro |
| 2 | A correctly sized, clean drawing | Why it measures 80 × 40, not 2032 × 1016 |
| 3 | A working copy with layers and leads | Which material is waste, and how the path differs from the drawing |
| 4 | A correctly ordered simulation | How the two holes and outer profile form one job |

If you have not installed the software, read the illustrated examples first. Then repeat the exercises in the software that matches your machine. [Chapter 1](01-bochu-systems.md) explains the installation and version choices.

## What changes at the machine

A corner in the drawing does not automatically correspond to a corner of the sheet. Machine work adds coordinate referencing, sheet location, nozzle and gas checks, recipe selection, travel checks and first-part inspection. Chapters 5–10 follow that progression.

One distinction matters immediately: simulation plays the path on screen; a dry run moves the real machine. Before using an unfamiliar machine, complete its operating instruction and understand its guarding, stopping controls and startup procedure. Memorising a short checklist is not a substitute for that knowledge.

## Reading the illustrations

The dimensioned blue drawings are original exercise diagrams. The dark software illustrations come from Bochu’s classic CypCut tutorials. Their captions explain what to inspect. CypCutE and CypCutPro may arrange controls differently; use the matching software manual when the screen differs.

This edition has not been validated through a complete software session or a live cutting trial. You can learn the documented concepts now. Missing machine parameters are left unresolved rather than replaced with arbitrary defaults.

## Your first exercise

Download the file, then identify the material that will remain in the finished part and the material that becomes waste.

<details>
<summary>Compare your answer</summary>

The retained part lies inside the rectangle and outside both circles. The surrounding sheet and the two hole slugs are waste. This distinction determines lead placement and offset direction.

</details>

Reference: [Bochu quick-start workflow](https://www.bochu.com/tutorials/quick-start-operation-flow/). Dimensions come from the project’s exercise file.

---

[Contents](README.md) · [Find your software and workspace →](01-bochu-systems.md)

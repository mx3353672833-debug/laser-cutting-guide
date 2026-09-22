# 13 · Three Complete Practice Projects

[简体中文](../zh-CN/13-three-projects.md) | [English](./13-three-projects.md)

[Previous / Daily Checks, Consumables, and Maintenance Boundaries](12-maintenance-boundaries.md) · [Next / Trade Shows and Customer Site Demos](14-demo-events.md)

## What you will learn

Finish **prep, simulation, and inspection plans** for three projects. Beam-on needs supervision; offline parts can be done first.

## Project A · Double-hole plate (running case)

![ex01](../../assets/previews/en/ex01-double-hole-plate.png)

*Figure 13-1 Project A preview.*

**Tasks**

1. Open `exercises/dxf/ex01-double-hole-plate.dxf` (80×40, two Ø8 holes, offline geometry).  
2. Check units and closure.  
3. Leads: into holes / out of frame.  
4. Kerf: your measured value (mark trial value as pending).  
5. Micro joints on non-mating edges; demo a cooling point on a sharp corner.  
6. Order: holes → outer.  
7. Simulate.  
8. Fill the first-article plan (plan only if not cutting).

**Checks**

- Say 80×40 and 2 holes.  
- Inner first.  
- Micro joint ≠ cooling point.  
- Simulation does not move the machine.

## Project B · Text / name plate

**Tasks**

1. Outline + mounting hole + text (e.g. P-01).  
2. If text is mark-only: map to mark or **do-not-machine** target layer.  
3. Keep leads away from text.  
4. Simulate order: text/mark → hole → outer (or your process).

**Checks**

- Four-step layer chain.  
- MARK name does not auto-mark.  
- Inspection: text height, hole position, outline.

## Project C · Multi-part layout

![ex08](../../assets/previews/en/ex08-multi-part-layout.png)

*Figure 13-2 Project C preview (3 single-hole parts + SHEET).*

**Tasks**

1. Open ex08.  
2. Nest inside SHEET with edge margin (site-defined).  
3. Exclude SHEET/NOTE from cutting.  
4. Order: each hole → each outer.  
5. Simulate part count = 3.

**Checks**

- Say “3 parts, one hole each”.  
- Stock frame not in toolpath.  
- Explain part order to reduce rapids.

## Answers and acceptance (summary)

See `exercises/answers/en/`. Score observable outcomes: sizes match design, gaps found, simulate order correct — not “I understood it”.

## Sources

Exercise DXF geometry report; CypCutE/Pro process and sorting sections.

---

[Previous / Daily Checks, Consumables, and Maintenance Boundaries](12-maintenance-boundaries.md) · [Next / Trade Shows and Customer Site Demos](14-demo-events.md)

[简体中文](../zh-CN/13-three-projects.md) | [English](./13-three-projects.md)

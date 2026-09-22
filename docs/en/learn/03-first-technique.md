# 03 · First technique (lead / kerf / micro joint / cooling point)

[简体中文](../../zh-CN/learn/03-first-technique.md) | [English](./03-first-technique.md)

> **Result**: leads, offset path, micro joints on non-mating edges, cooling points on corners.

## Four actions

| Do | Where | Success looks like |
|---|---|---|
| Add leads | technique / lead | short entry tails |
| Kerf offset | technique / compensate | path shifted ~½ kerf |
| Micro joint | technique / micro joint | gaps on path |
| Cooling point | technique / cooling point | solid dots on path |

![Technique panel (official)](../../../assets/screenshots/bochu-cypcut/technique-panel.png)

### 1. Leads

![Lead (official)](../../../assets/screenshots/bochu-cypcut/lead-line.png)

1. Select two holes → add lead from **inside scrap**.  
2. Outer frame → lead from **outside**.  
3. Success: entry tails appear.  
4. Check: tails do not cross other parts.

### 2. Kerf

![Kerf (official)](../../../assets/screenshots/bochu-cypcut/kerf-comp.png)

1. Open kerf compensation.  
2. Start with table/default; **measure later**.  
3. Outer grows, inner shrinks.  
4. Success: path offset from design.  
5. Wrong direction makes size worse — flip it.

### 3. Micro joints (anti-tip)

![Micro joint (official)](../../../assets/screenshots/bochu-cypcut/micro-joint.png)

1. Put 1–2 joints on **outer non-mating edges**.  
2. Success: **gaps** on path (not solid dots).  
3. Do not put joints on holes.

### 4. Cooling points (anti-burn) ← not micro joints

![Cooling point (official)](../../../assets/screenshots/bochu-cypcut/cooling-point.png)

1. Put cooling points on **sharp corners**.  
2. Success: **solid dots**.  

| | Mark | Purpose | At that point |
|---|---|---|---|
| Micro joint | gap | stop tip/crash | laser off, leave link |
| Cooling point | solid dot | stop corner burn | dwell + off + gas cool |

## Self-check

- [ ] Leads: into holes / out of frame  
- [ ] Kerf: outer grow, inner shrink  
- [ ] Joints on non-mating outer edges  
- [ ] Cooling dots on corners  
- [ ] Can explain joint vs cooling  

**Chain**: leads avoid scars → kerf fills the slit → joints stop tipping → cooling stops corner burn.

Next: [04 First precheck](04-first-precheck.md)

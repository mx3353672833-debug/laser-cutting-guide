# 01 · UI tour (real screenshots)

[简体中文](../../zh-CN/learn/01-ui-tour.md) | [English](./01-ui-tour.md)

> **Goal**: look at official screenshots and point to the same five regions on your screen.  
> Screenshots come from **Bochu’s official CypCut tutorials**. CypCutE / CypCutPro may differ in layout, but regions are the same. Trust the text **on your screen**.

## 1. Five regions

```text
+------------------------------------------+
| Menus (File Draw Technique CNC ...)      |
+------------------------------------------+
|                                          |
|           Drawing board (parts)          |
|                                          |
+------------------------------------------+
| Control panel: Start Pause Stop ...      |
| Alarms / logs                            |
+------------------------------------------+
```

## 2. Control panel

![CypCut control panel (official)](../../../assets/screenshots/bochu-cypcut/control-panel.png)

*Figure 01-1 · Source: Bochu Machining Control.*

| Action | What happens | Success looks like |
|---|---|---|
| Start | machine cuts (laser on) | path advances |
| Pause | freeze | can step fwd/back |
| Stop | end run | head returns to preset |
| Simulate / preview | screen only | **no motion** |
| Frame / dry run | machine empty run | **moves, no laser** |

## 3. Coordinates

![Coordinates (official)](../../../assets/screenshots/bochu-cypcut/coordinates.png)

*Figure 01-2 · floating origin = head now; work origin = fixed bed zero.*

## 4. Three prechecks

![Manual check (official)](../../../assets/screenshots/bochu-cypcut/manual-check.png)

![Preview position (official)](../../../assets/screenshots/bochu-cypcut/preview-position.png)

![Frame / Border / Dry Run (official)](../../../assets/screenshots/bochu-cypcut/frame-border-dryrun.png)

*Figures 01-3…01-5 · Machining Precheck.*

| Name | Path | Machine |
|---|---|---|
| Frame | bounding box | moves |
| Border | outer contour | moves |
| Dry Run | full toolpath | moves, laser/gas off |

## 5. Technique area

![Technique panel (official)](../../../assets/screenshots/bochu-cypcut/technique-panel.png)

![Layer cut params (official)](../../../assets/screenshots/bochu-cypcut/layer-cut.png)

*Figures 01-6…01-7.*

## 6. Alarms

![Alarm bar (official)](../../../assets/screenshots/bochu-cypcut/alarm-title.png)

*Figure 01-8.*

If alarmed: **stop** → copy the raw text → check [stuck guide](00-stuck.md) → if unclear, stop and hand off with the text.

## 7. 3-minute drill (no machine)

1. Open software or demo mode.  
2. Point to drawing board, control panel, alarm bar.  
3. Find **Simulate** (do not press Start).  
4. Note where Start/Pause/Stop live on **your** screen.

**Pass**: name 5 regions; know simulate does not move the machine.

Next: [02 First import](02-first-import.md)

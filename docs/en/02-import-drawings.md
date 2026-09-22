# 02 · Clean and check the drawing

[简体中文](../zh-CN/02-import-drawings.md) · [English](./02-import-drawings.md)

Leave gas pressure, power and compensation alone for now. The task is to establish that the drawing represents the part you intend to make. Start with the [two-hole plate](../../exercises/dxf/ex01-double-hole-plate.dxf), keeping an unchanged original and a working copy.

## 1. Load one copy into an empty document

Bochu’s classic tutorial uses File → Import to append geometry. For a fresh exercise, Open can load a single file instead. Do not import the same plate again into an occupied drawing board.

![Classic CypCut import menu](../../assets/screenshots/bochu-cypcut/import-dialog.png)

*Locate File and the Import row. Reading the file is only the first step; it does not establish that the geometry is correct.*

Fit all geometry into view. Find one rectangle, two circles and a text label. In ex01 the label belongs to the MARK source layer. This exercise cuts the profiles only; we will explicitly exclude the label next chapter. If nothing is visible, check that a file loaded and fit the view before importing it again.

## 2. Measure an edge and a hole

Use the distance tool in your version and snap to the endpoints of the long edge. Expect 80 mm, and 40 mm on the short edge. Read a circle’s properties: diameter 8 mm, or radius 4 mm. A radius field showing 4 does not mean a 4 mm hole.

![Plate dimensions](../../assets/figures/en/workpiece.svg)

The circle centres are (20,20) and (60,20), giving 40 mm centre spacing. These describe drawing geometry, not the position on the machine.

Open [ex02, wrong units](../../exercises/dxf/ex02-wrong-units.dxf). Its coordinate values still describe an 80 × 40 rectangle, but the file declares inches. An importer that converts that declaration to millimetres will produce 2032 × 1016. Software that ignores the declaration may still display 80 × 40. Record what your importer actually does; the exercise does not require the drawing to enlarge.

Once you establish the intended units, reinterpret the import units where supported. If scaling is needed, derive the factor from the measured result. Do not divide a correctly displayed 80 × 40 drawing by 25.4. Resolve scale before adding process geometry that may need rebuilding afterward.

## 3. Find the disconnected endpoints

[Ex04](../../exercises/dxf/ex04-open-contour.dxf) almost forms a rectangle, but has a gap at the lower left.

![Ex04 lower-left gap](../../assets/previews/en/ex04-open-contour.png)

Zoom in: the vertical line ends at (0,2), while the bottom edge ends at (0,0). The gap is 2 mm. Use your version’s open-contour selection or display tool, then draw the missing segment or extend the correct geometry after confirming the design intent. Recheck closure afterward. Two endpoints can look connected at a small zoom level without being connected geometrically.

Whether a merge command closes this gap depends on tolerance. Increasing tolerance arbitrarily may connect other features that should stay separate. Repairing this known gap explicitly makes the change easy to verify.

## 4. One visible edge can contain three entities

The bottom edge in [ex03](../../exercises/dxf/ex03-duplicate-lines.dxf) consists of an edge of the closed rectangle plus two coincident LINE entities. It looks like one edge but can create repeated travel if left untreated.

Keep a copy, remove duplicates, and check that only one effective path remains on the bottom edge. Inspect simulation for repeated passes. Merging connected lines changes connectivity; removing duplicates resolves overlapping entities.

[Ex05](../../exercises/dxf/ex05-tiny-entities.dxf) contains a 0.05 mm line and a circle of radius 0.03 mm. Use it to observe a small-entity removal threshold. A small feature on a production drawing may be intentional, so automatic cleanup still requires judgement.

## Record the result

| Check | Expected for ex01 |
|---|---|
| Overall size | 80 × 40 mm |
| Holes | Two, diameter 8 mm |
| Centre spacing | 40 mm |
| Profiles | Closed and correctly positioned |
| Duplicates/debris | No unwanted machining entities |
| Text label | Identified for exclusion from machining |

Save the checked working copy. Next, we add process geometry to that file.

<details>
<summary>Check your understanding: what do 2032, 4 and 2 describe?</summary>

2032 mm may result from interpreting 80 drawing units as inches. In ex01, 4 mm is the circle radius, not the diameter. In ex04, 2 mm is the gap length. Identify the object and unit before making a correction.

</details>

References: CypCutE V7.1 §1.4.2; [official import tutorial](https://www.bochu.com/tutorials/basics-import-drawing/); original exercise geometry.

---

[← Find your software and workspace](01-bochu-systems.md) · [Contents](README.md) · [Put the toolpath in the right place →](03-leads-kerf-microjoints.md)

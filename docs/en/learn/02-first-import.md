# 02 · First import (follow along)

[简体中文](../../zh-CN/learn/02-first-import.md) | [English](./02-first-import.md)

> **Result**: a 80×40 plate with two holes is on the board and measures correctly.  
> Need: PC + software (or demo mode) + [ex01 DXF](../../../exercises/dxf/ex01-double-hole-plate.dxf)

## Prepare

| Need | Where | Why |
|---|---|---|
| Cutting software | machine PC or demo mode | import |
| ex01 file | exercises/dxf/ | practice |
| Notes app | phone | record size/version |

## Steps (click → expect)

### 1. Import

1. **File > Import**  
2. Pick `ex01-double-hole-plate.dxf`  
3. **Success**: rectangle + two circles  
4. **Fail**: empty board → see stuck guide

![Import dialog (official)](../../../assets/screenshots/bochu-cypcut/import-dialog.png)

*Figure 02-1 official Import UI.*

### 2. Measure immediately

1. Use measure/dimension tool  
2. Click the long edge → about **80** mm  
3. Width → about **40**  
4. If ~2032 → read as inches (×25.4). Fix units first. **Do not edit kerf yet.**

### 3. Inner vs outer

![Inner/outer (official)](../../../assets/screenshots/bochu-cypcut/inner-outer.png)

*Figure 02-2.*

### 4. Save

Save as `ex01-YYYY-MM-DD` + software-native extension.

## Self-check

- [ ] Says 80 by 40  
- [ ] Points out holes vs outer  
- [ ] Knows inch mistake inflates 25.4×  
- [ ] File saved  

**Chain**: import → **measure first** → inner/outer → save.

Next: [03 First technique](03-first-technique.md)

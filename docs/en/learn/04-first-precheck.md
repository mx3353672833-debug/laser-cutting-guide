# 04 · First precheck (simulate / frame / dry run)

[简体中文](../../zh-CN/learn/04-first-precheck.md) | [English](./04-first-precheck.md)

> **Result**: correct order, range on stock, know what moves. **Fully doable on the PC.**

## Sort first (inner then outer)

1. Open sort / toolpath planning.  
2. Target: **hole1 → hole2 → outer**.  
3. Success: numbers 1,2,3 are holes before outer.  
4. Wrong: outer first → parts drop.

## Three checks

| Action | Machine | Watch |
|---|---|---|
| Simulate | **no move** | path shape/order |
| Frame | **moves** | pointer/path on stock? |
| Dry Run | **moves** | collisions / envelope |

![Frame/Border/DryRun (official)](../../../assets/screenshots/bochu-cypcut/frame-border-dryrun.png)

![Preview position (official)](../../../assets/screenshots/bochu-cypcut/preview-position.png)

### A. Software simulate (now)

1. Press **Simulate**.  
2. Success: 1→2→3 as planned.  
3. Count **3** contour paths.

### B. Frame / dry run (when a machine is free)

1. Stock loaded, people clear.  
2. Frame → red pointer inside stock.  
3. Dry run → no fixture/rack crash.  
4. Fail → **stop**, move part/stock; do not force cut.

## Self-check

- [ ] Order hole→outer  
- [ ] Simulate does not move machine  
- [ ] Know frame/dry run move  
- [ ] 3 paths in simulate  

**Chain**: inner first → simulate order → frame range → dry run collisions.

Next: [05 First on-machine](05-first-on-machine.md)

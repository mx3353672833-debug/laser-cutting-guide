# 05 · First on machine (memorize before you move)

[简体中文](../../zh-CN/learn/05-first-on-machine.md) | [English](./05-first-on-machine.md)

> Most people learn by watching, then try alone. This is **your safety checklist**, not a forever babysitter.  
> Buttons differ per machine; **order follows that machine SOP / labels**.

## 60-second recite (do not cut until pass)

1. **Where is the e-stop?**  
2. **Guard closed?**  
3. **Exhaust on?**  
4. **Chiller/gas alarms clear?**  
5. **Software alarm bar empty?**  
6. **If unsure → stop. Do not guess buttons.**

## Safe first solo flow

| # | Do | Success | Fail |
|---|---|---|---|
| 1 | Power on per SOP | panel normal | stop, read SOP |
| 2 | **Home** | coordinates built | clear other alarms first |
| 3 | Jog axes slowly | directions correct | e-stop |
| 4 | Load plate, close guard | flat, closed | — |
| 5 | **Find edge** (low tilt) | angle/zero | wrong size can crash |
| 6 | Frame | pointer on stock | move |
| 7 | Dry run | no crash | fix |
| 8 | Cut first part with **site-verified row** | through | stop, log |
| 9 | Measure + photo | data | do not batch |

![Find edge (official)](../../../assets/screenshots/bochu-cypcut/find-edge.png)

![Find edge steps (official)](../../../assets/screenshots/bochu-cypcut/find-edge-steps.png)

*Figures 05-1/05-2. Official notes: home first, correct sheet size, tilt ≲10°, head on plate.*

## Where process numbers come from

1. Ask: is there a **verified row for this stock**?  
2. Yes → copy the **whole row** (thickness, nozzle, gas, speed, power, pressure, focus).  
3. No → **do not invent**; wait for a full row.  
4. Log parameters + result after the cut.

## If something goes wrong

| Symptom | Do | Don’t |
|---|---|---|
| Red alarm | stop, copy text | reset spam |
| Incomplete cut | stop, check nozzle/speed/row | endless extra pressure |
| Wrong size | check kerf direction/units | change everything blind |
| Noise/crash | **e-stop** | press start again |

## Self-check

- [ ] Can recite the 60-second list  
- [ ] Order: home → edge → frame → dry run → cut  
- [ ] Process rows copied whole  
- [ ] Alarm = stop  

**Chain**: recite → home → edge → frame → dry run → verified row first cut → measure and log.

Stuck? [00-stuck](00-stuck.md)

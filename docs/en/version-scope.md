# Version scope · 版本范围

[简体中文](../zh-CN/version-scope.md) | [English](./version-scope.md)

## Three version fields

| Field | Meaning | Example |
|---|---|---|
| Document / manual version | cover or revision log | CypCutE manual “Version 7.1” |
| Based-on software version | preface “based on …” | CypCutE **6.4.2310** |
| Runtime version | About page on the PC | **not measured here** |

## Matrix used in this guide

| Software | Doc | Based-on | Offline | Role here |
|---|---|---|---|---|
| CypCutE | V7.1 | 6.4.2310 | no control card → demo mode | **software track 00–04** |
| CypCutPro | V1.0.0 | 7.1.2432.5 (preface) | no control card → demo mode | **controls / calibration / micro joints & cooling points** |
| CypCut | V6.3.6 doc | 6.3.x | no Dog → DEMO | English tutorial concepts |
| HypCut | V1.7 | 2024A-1.0.2410.4 | no demo wording found | concepts only |
| XC3000S | User Manual V1.2 | — | simulation edition without dongle (that manual) | ch. 15 |
| XC3000Plus | Commissioning V1.3 | — | revision “dongle removed as standard” | ch. 15, pending |

Do **not** splice CypCutE 6.4.2310 click paths with CypCutPro 7.1.x paths.  
Do **not** merge cross-brand power-on or calibration into one flow.  
Installation energizing tests ≠ daily power-on.

## Key corrections kept

1. Ordinary / seamless micro joints vs cooling points.  
2. Gauge setting vs process pressure.  
3. DXF layer names do not auto-assign process.  
4. SHEET/NOTE must be checked non-cutting.  
5. Nozzle tables are conditional references (with exceptions).  
6. Empower licensing is per model.  
7. Demo mode, screen simulate, and machine dry run stay separate.

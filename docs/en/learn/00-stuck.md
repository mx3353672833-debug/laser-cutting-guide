# Stuck guide (symptom → where to look)

[简体中文](../../zh-CN/learn/00-stuck.md) | [English](./00-stuck.md)

| Symptom | Look at | Do |
|---|---|---|
| DXF will not import | format / path | re-export standard DXF |
| Size off by 25.4× | inch/mm units | fix units, **measure again** |
| Size slightly off | kerf direction/width | measure kerf; outer grow inner shrink |
| Open contours | merge/open check | join ends |
| Double cuts | duplicate lines | dedupe |
| Wrong order in simulate | sort | inner first |
| Can’t find micro joint / cooling point | Technique menu | lesson 03 screenshots |
| Will the machine move? | lesson 01 table | simulate no; frame/dry run yes |
| UI ≠ screenshots | CypCut vs E vs Pro | same regions; trust **your** labels |
| Red alarm | copy raw text | stop; manual; no force cut |
| Afraid at the machine | lesson 05 60-second list | if you can’t recite, don’t cut |

Still stuck? Open a **Learning question** issue: lesson id, About version, what you see.

# ex07 Layer process · Answer

| Source layer | Content |
|---|---|
| CUT | 70×35 outline + hole r=5 |
| MARK | short lines + text P-01 |
| TEXT0 | text “center text do not cut” |

**Answer (mapping semantics)**: these are **DXF source names**. Map them to **target layers** after import. Suggested: CUT→normal cut layer; MARK→mark/first-order layer with process; TEXT0→**do not machine**.  
Names do not auto-assign process.

**Criteria**: write source → map → target → layer process; no “TEXT0 never cuts because of the name”.

<details>
<summary>Scoring</summary>

- Four-step chain complete
- Source name ≠ process

</details>

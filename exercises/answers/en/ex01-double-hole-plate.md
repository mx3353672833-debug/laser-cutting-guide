# ex01 Double-hole plate · Answer

| Item | Parsed value |
|---|---|
| Size | outline **80×40** (INSUNITS=4=mm) |
| Holes | **2** circles r=**4** (Ø8) at (20,20)(60,20) |
| Layers | CUT outline+holes; MARK text |
| Closed | outer LWPOLYLINE closed=true |

**Key tasks**: units/size; inner vs outer; leads; inner first; simulate.  
**Answer**: 80 by 40; two inner holes; holes → outer.  
**Criteria**: sizes correct; inner first; simulate does not move machine or fire laser.

<details>
<summary>Scoring</summary>

- Matches JSON geometry
- Outer/inner correct
- No safety errors

</details>

# ex02 Wrong units · Answer

The coordinates match ex01: an 80×40 outline and two Ø8 holes. The header deliberately declares inches (`$INSUNITS=1`). The result depends on whether the importer converts those declared units.

| Imported outline | Interpretation | Next action |
|---|---|---|
| 2032×1016 mm | Converted inches to millimeters, a factor of 25.4 | Preserve the source; reimport with millimeter interpretation and measure again |
| 80×40 mm | No unit scaling occurred on this import | Do not shrink it again; check the import settings and Ø8 hole |
| Another size | Another scale or import setting is involved | Record the settings and investigate before editing |

<details>
<summary>How to check your answer</summary>

Read the length, height and one hole diameter. Explain why your importer did or did not apply a factor of 25.4. The final geometry should be 80×40 mm with 8 mm holes. Changing a unit label may not rescale existing coordinates; measure after every correction.

</details>

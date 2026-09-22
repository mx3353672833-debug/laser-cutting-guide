# Laser Cutting Guide · 激光切割操作入门

[简体中文](docs/zh-CN/README.md) | [English](docs/en/README.md)

Bilingual practical guide v0.1 for laser-cutting sales people: prepare machining files (Bochu first), complete a supervised first article, run simple demos, then migrate concepts to Raytools / Empower.

中英文双语实操教程 v0.1：先学柏楚准备加工文件与带教上机，再迁移到嘉强。

## Start

| Language | Start here |
|---|---|
| 简体中文 | [docs/zh-CN/00-start-here.md](docs/zh-CN/00-start-here.md) |
| English | [docs/en/00-start-here.md](docs/en/00-start-here.md) |

## What is inside

- 16 chapters (00–15) in both languages
- 12 shared diagrams, 8 DXF exercises with previews and answers
- Fill-in templates, glossary, version scope, sources, known gaps
- Local checker `scripts/check_content.py` and GitHub Actions

## Safety and scope

- First machine work must be supervised by someone who knows **that** machine.
- Demo mode / software simulation is not beam-on control.
- Process numbers stay tied to material, thickness, head, nozzle, gas, and a verified process row.
- v0.1 is not a vendor certified course and has not been validated on a live machine.

## Repository layout

```text
docs/zh-CN  docs/en     chapters and extras
assets/figures  previews
exercises/dxf  answers  scripts
templates/zh-CN  en
scripts/check_content.py
```

## Check locally

```bash
python3 scripts/check_content.py
```

## License and attribution

Original tutorial text and original diagrams in this repository: see [LICENSE-POLICY.md](LICENSE-POLICY.md).  
Third-party manuals and vendor pages are **not** redistributed here; see [ATTRIBUTION.md](ATTRIBUTION.md).

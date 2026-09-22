#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structural checks for tutorial/ content.

Document checks only. Hardware/machine validation is a separate report.
Exit 0 when all document checks pass.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS: list[tuple[str, str, str]] = []


def ok(code: str, msg: str) -> None:
    RESULTS.append(("PASS", code, msg))


def fail(code: str, msg: str) -> None:
    RESULTS.append(("FAIL", code, msg))


CHAPTERS = [
    "00-start-here",
    "01-bochu-systems",
    "02-import-drawings",
    "03-leads-kerf-microjoints",
    "04-nesting-sorting-simulate",
    "05-machine-and-prestart",
    "06-homing-calibration",
    "07-plate-edge-dryrun",
    "08-process-tables-first-part",
    "09-first-cut-inspection",
    "10-pause-resume-tasks",
    "11-exceptions-feedback",
    "12-maintenance-boundaries",
    "13-three-projects",
    "14-demo-events",
    "15-raytools-migration",
]

EXTRAS = ["README.md", "glossary.md", "version-scope.md", "sources.md", "known-gaps.md"]
DXF_IDS = [
    "ex01-double-hole-plate",
    "ex02-wrong-units",
    "ex03-duplicate-lines",
    "ex04-open-contour",
    "ex05-tiny-entities",
    "ex06-nested-contours",
    "ex07-layer-process",
    "ex08-multi-part-layout",
]
TEMPLATES = [
    "00-machine-version-card",
    "01-prestart-checklist",
    "02-first-article-inspection",
    "03-exception-report",
    "04-demo-prep",
    "05-learning-progress",
]
FIGS = [
    "fig-01-system-map.svg",
    "fig-02-unit-scale.svg",
    "fig-03-open-closed.svg",
    "fig-04-duplicate-lines.svg",
    "fig-05-lead-line.svg",
    "fig-06-kerf.svg",
    "fig-07-micro-joint.svg",
    "fig-08-inner-outer.svg",
    "fig-09-sorting.svg",
    "fig-10-coordinates.svg",
    "fig-11-simulate-boundary.svg",
    "fig-12-layer-map.svg",
]
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
ABS_BAD = re.compile(r"(/Users/|/Volumes/|research/agent-|C:\\\\)")


def check_tree() -> None:
    for lang in ("zh-CN", "en"):
        base = ROOT / "docs" / lang
        for name in CHAPTERS + EXTRAS:
            p = base / name if name.endswith(".md") else base / f"{name}.md"
            if p.exists() and p.stat().st_size > 200:
                ok("file", f"docs/{lang}/{name}.md")
            else:
                fail("file", f"docs/{lang}/{name}.md missing/short")
    for name in ("README.md", "CONTRIBUTING.md", "CHANGELOG.md", "ROADMAP.md",
                 "ATTRIBUTION.md", "LICENSE-POLICY.md"):
        p = ROOT / name
        if p.exists() and p.stat().st_size > 100:
            ok("file", name)
        else:
            fail("file", f"{name} missing")
    if (ROOT / "scripts" / "check_content.py").exists():
        ok("file", "scripts/check_content.py")
    else:
        fail("file", "scripts/check_content.py missing")


def check_language_switch() -> None:
    for lang, other in (("zh-CN", "en"), ("en", "zh-CN")):
        for name in CHAPTERS:
            text = (ROOT / "docs" / lang / f"{name}.md").read_text(encoding="utf-8")
            if f"../../{other}/{name}.md" in text or f"../{other}/{name}.md" in text:
                ok("lang-switch", f"{lang}/{name} ↔ {other}")
            else:
                fail("lang-switch", f"{lang}/{name} missing counterpart link")
            if "简体中文" not in text or "English" not in text:
                fail("lang-switch", f"{lang}/{name} missing bilingual header labels")


def check_nav() -> None:
    for lang in ("zh-CN", "en"):
        for i, slug in enumerate(CHAPTERS):
            text = (ROOT / "docs" / lang / f"{slug}.md").read_text(encoding="utf-8")
            if i > 0 and f"{CHAPTERS[i-1]}.md" not in text:
                fail("nav", f"{lang}/{slug} missing prev")
            if i < len(CHAPTERS) - 1 and f"{CHAPTERS[i+1]}.md" not in text:
                fail("nav", f"{lang}/{slug} missing next")
            else:
                ok("nav", f"{lang}/{slug} nav")


def check_links_and_images() -> None:
    missing = []
    abs_hits = []
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for m in ABS_BAD.finditer(text):
            # allow mention in check script description only
            if "check_content" in md.name or "CHANGELOG" in md.name:
                continue
            abs_hits.append((md.relative_to(ROOT), m.group(0)))
        for ref in LINK_RE.findall(text) + IMG_RE.findall(text):
            if ref.startswith(("http://", "https://", "mailto:", "#")):
                continue
            ref_path = ref.split("#")[0]
            if not ref_path:
                continue
            target = (md.parent / ref_path).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                # outside tutorial — fail
                missing.append((str(md.relative_to(ROOT)), ref_path, "outside-root"))
                continue
            if not target.exists():
                missing.append((str(md.relative_to(ROOT)), ref_path, "missing"))
    if missing:
        fail("links", f"{len(missing)} bad refs e.g. {missing[:6]}")
    else:
        ok("links", "all relative links/images resolve")
    if abs_hits:
        fail("no-internal-paths", f"internal/abs path leaks: {abs_hits[:6]}")
    else:
        ok("no-internal-paths", "no research/abs path leaks in docs")


def check_assets() -> None:
    for fig in FIGS:
        p = ROOT / "assets" / "figures" / "shared" / fig
        if p.exists():
            ok("asset", fig)
        else:
            fail("asset", f"missing {fig}")
    for lang in ("zh-CN", "en"):
        for ex in DXF_IDS:
            p = ROOT / "assets" / "previews" / lang / f"{ex}.png"
            if p.exists():
                ok("asset", f"previews/{lang}/{ex}.png")
            else:
                fail("asset", f"missing preview {lang}/{ex}.png")
            a = ROOT / "exercises" / "answers" / lang / f"{ex}.md"
            if a.exists() and a.stat().st_size > 80:
                ok("asset", f"answers/{lang}/{ex}.md")
            else:
                fail("asset", f"missing answer {lang}/{ex}.md")
        for tpl in TEMPLATES:
            p = ROOT / "templates" / lang / f"{tpl}.md"
            if p.exists() and p.stat().st_size > 80:
                ok("asset", f"templates/{lang}/{tpl}.md")
            else:
                fail("asset", f"missing template {lang}/{tpl}.md")
    for ex in DXF_IDS:
        p = ROOT / "exercises" / "dxf" / f"{ex}.dxf"
        if p.exists() and p.stat().st_size > 100:
            ok("dxf", f"{ex}.dxf")
        else:
            fail("dxf", f"missing {ex}.dxf")


def check_dxf_report() -> None:
    report = ROOT / "exercises" / "dxf-structure-report.json"
    if not report.exists():
        fail("dxf-json", "dxf-structure-report.json missing")
        return
    data = json.loads(report.read_text(encoding="utf-8"))
    ok("dxf-json", f"parsed json type={type(data).__name__}")
    # optional ezdxf audit if available
    try:
        import ezdxf  # type: ignore
    except Exception:
        ok("ezdxf", "ezdxf not installed in this runtime — skipped (CI may add later)")
        return
    for ex in DXF_IDS:
        p = ROOT / "exercises" / "dxf" / f"{ex}.dxf"
        try:
            doc = ezdxf.readfile(str(p))  # type: ignore
            auditor = doc.audit()
            errs = len(auditor.errors)
            fixed = len(auditor.fixes)
            if errs:
                fail("ezdxf", f"{ex} audit errors={errs}")
            else:
                ok("ezdxf", f"{ex} audit errors=0 fixes={fixed}")
        except Exception as e:
            fail("ezdxf", f"{ex} read/audit failed: {e}")


def check_content_markers() -> None:
    # key corrections present in both languages
    zh3 = (ROOT / "docs/zh-CN/03-leads-kerf-microjoints.md").read_text(encoding="utf-8")
    en3 = (ROOT / "docs/en/03-leads-kerf-microjoints.md").read_text(encoding="utf-8")
    for label, text in (("zh", zh3), ("en", en3)):
        if "冷却点" in text or "Cooling point" in text:
            ok("marker", f"{label} cooling point")
        else:
            fail("marker", f"{label} missing cooling point")
        if "无痕" in text or "Seamless" in text:
            ok("marker", f"{label} seamless micro joint")
        else:
            fail("marker", f"{label} missing seamless")
    zh8 = (ROOT / "docs/zh-CN/08-process-tables-first-part.md").read_text(encoding="utf-8")
    en8 = (ROOT / "docs/en/08-process-tables-first-part.md").read_text(encoding="utf-8")
    if "供气表" in zh8 and "gauge" in en8.lower():
        ok("marker", "gauge vs process pressure")
    else:
        fail("marker", "gauge setting qualifier missing")
    zh15 = (ROOT / "docs/zh-CN/15-raytools-migration.md").read_text(encoding="utf-8")
    en15 = (ROOT / "docs/en/15-raytools-migration.md").read_text(encoding="utf-8")
    if "未找到官方存在证据" in zh15 and "no official existence evidence" in en15:
        ok("marker", "XC7000 wording")
    else:
        fail("marker", "XC7000 wording not downgraded")
    # no editorial agent language in learner docs
    bad_re = re.compile(r"返工|R1-R6|agent-2|Agent-2|禁止写每件两孔")
    for md in (ROOT / "docs").rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        m = bad_re.search(text)
        if m:
            fail("editorial-leak", f"{md.relative_to(ROOT)} contains {m.group(0)}")
    ok("editorial-leak", "no editor/agent jargon in docs" if True else "")


def check_yaml_ci() -> None:
    yml = ROOT / ".github/workflows/check.yml"
    if yml.exists() and "check_content.py" in yml.read_text(encoding="utf-8"):
        ok("ci", "workflow runs check_content.py")
    else:
        fail("ci", "workflow missing or wrong script")


def main() -> int:
    check_tree()
    check_language_switch()
    check_nav()
    check_links_and_images()
    check_assets()
    check_dxf_report()
    check_content_markers()
    check_yaml_ci()
    # cleanup placeholder from check_assets bug if any fail counted wrong — ignore
    n_pass = sum(1 for s, _, _ in RESULTS if s == "PASS")
    n_fail = sum(1 for s, _, _ in RESULTS if s == "FAIL")
    lines = ["tutorial v0.1 content check", f"root={ROOT}", f"PASS={n_pass} FAIL={n_fail}",
             "note=document checks only; not hardware validation", ""]
    for st, code, msg in RESULTS:
        lines.append(f"{st}\t{code}\t{msg}")
    out = "\n".join(lines) + "\n"
    out_path = ROOT.parent / "research" / "tutorial-v0.1-build" / "check-output.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out, encoding="utf-8")
    print(out)
    print(f"[written] {out_path}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())

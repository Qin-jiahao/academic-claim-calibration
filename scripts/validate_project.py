#!/usr/bin/env python3
"""Dependency-free checks for the bilingual academic-claim-calibration project."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path}: invalid UTF-8 ({exc})")
        return ""


def check_skill() -> None:
    path = ROOT / "skills" / "academic-claim-calibration" / "SKILL.md"
    text = read(path)
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        fail(f"{path}: missing YAML frontmatter")
        return
    frontmatter = text.split("---\n", 2)[1]
    name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.M)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
    if not name or name.group(1) != "academic-claim-calibration":
        fail(f"{path}: invalid name")
    if not description or not description.group(1).strip():
        fail(f"{path}: missing description")
    required = (
        "适用场景",
        "使用边界",
        "必需输入",
        "工作流程",
        "输出格式",
        "质量检查",
        "局限性",
        "完整输入示例",
        "信息不足时的处理示例",
        "来源",
    )
    for section in required:
        if section not in text:
            fail(f"{path}: missing section {section}")
    if "TODO" in text or "FIXME" in text:
        fail(f"{path}: unfinished marker found")


def check_prompt() -> None:
    path = ROOT / "prompts" / "academic-claim-calibration.md"
    text = read(path)
    required = (
        "使用场景",
        "输入要求",
        "输出要求",
        "禁止编造的内容",
        "信息不足时的处理",
        "双语示例",
        "来源",
        "Use case",
        "Input requirements",
        "Output requirements",
        "Fabrication ban",
    )
    for section in required:
        if section not in text:
            fail(f"{path}: missing section {section}")
    if "TODO" in text or "FIXME" in text:
        fail(f"{path}: unfinished marker found")


def check_links() -> None:
    for path in ROOT.rglob("*.md"):
        text = read(path)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local = (path.parent / target.split("#", 1)[0]).resolve()
            if not local.exists():
                fail(f"{path}: broken local link {target}")


def check_required_files() -> None:
    for relative in (
        "README.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "THIRD-PARTY-NOTICES.md",
        "docs/provenance.md",
        "docs/reference-basis.md",
        "docs/oral-practices.md",
        "skills/academic-claim-calibration/references/oral-practices.md",
        "scripts/validate_project.py",
    ):
        if not (ROOT / relative).exists():
            fail(f"missing required file: {relative}")


check_required_files()
check_skill()
check_prompt()
check_links()

if ERRORS:
    print("\n".join(ERRORS))
    sys.exit(1)

print("validated bilingual Skill, Prompt, provenance, references, and local links")

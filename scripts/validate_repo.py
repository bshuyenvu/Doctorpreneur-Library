#!/usr/bin/env python3
"""Validator cho Doctorpreneur Library.

Kiểm tra tính toàn vẹn cấu trúc của knowledge base:
  - Đủ 66 thư mục chương với README.md.
  - Sidebar liệt kê đủ 66 đường dẫn chương.
  - Không có liên kết Markdown nội bộ trỏ tới file không tồn tại.
  - Các file resource/case-study/community tồn tại.
  - Không lẫn ký tự Cyrillic (lỗi gõ nhầm thường gặp với tiếng Việt).

Chạy:  python scripts/validate_repo.py
Thoát 0 nếu không có lỗi; thoát 1 nếu có lỗi.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHAPTERS = [
    "01-doctorpreneur-mindset", "02-entrepreneurship", "03-lean-startup",
    "04-problem-discovery", "05-customer-discovery", "06-design-thinking",
    "07-clinical-workflow", "08-value-proposition", "09-business-model",
    "10-market-analysis", "11-competitive-intelligence", "12-health-economics",
    "13-reimbursement", "14-pricing-strategy", "15-go-to-market",
    "16-b2b-sales", "17-partnerships", "18-procurement",
    "19-healthcare-regulation", "20-medical-device-regulation", "21-fda-pathways",
    "22-eu-mdr", "23-quality-management", "24-risk-management",
    "25-clinical-evaluation", "26-clinical-trials", "27-evidence-generation",
    "28-research-methodology", "29-biostatistics", "30-real-world-evidence",
    "31-digital-health", "32-telemedicine", "33-mobile-health",
    "34-wearables-iot", "35-ehr-interoperability", "36-fhir-hl7",
    "37-medical-imaging", "38-clinical-decision-support", "39-cybersecurity",
    "40-privacy-governance", "41-ai-healthcare", "42-machine-learning",
    "43-deep-learning", "44-generative-ai", "45-nlp-clinical",
    "46-computer-vision", "47-ai-validation", "48-responsible-ai",
    "49-human-ai-interaction", "50-mlops-healthcare", "51-product-management",
    "52-user-experience", "53-software-architecture", "54-data-engineering",
    "55-devops-cloud", "56-product-analytics", "57-project-management",
    "58-team-building", "59-leadership", "60-fundraising",
    "61-financial-modeling", "62-legal-ip", "63-medical-education",
    "64-scaling-operations", "65-impact-ethics", "66-international-expansion",
]

RESOURCES = [
    "ai-tool-library", "book-library", "course-library", "open-source-library",
    "paper-library", "prompt-library", "sop-library", "template-library",
    "video-library",
]

CASE_STUDIES = ["babylon-health", "doximity", "idoven", "osler", "viz-ai", "zocdoc"]
COMMUNITY = ["conferences", "international-communities"]

# Regex tìm link Markdown [text](target); bỏ qua link ngoài (http, mailto) và neo (#...).
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CYRILLIC_RE = re.compile(r"[Ѐ-ӿ]")


def is_internal(target: str) -> bool:
    t = target.strip()
    if not t or t.startswith(("http://", "https://", "mailto:", "#", "tel:")):
        return False
    return True


def check_local_links(errors: list[str]) -> None:
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            target = m.group(1).split("#", 1)[0].strip()
            if not is_internal(target):
                continue
            # Đường dẫn tuyệt đối kiểu docsify (/foo) tính từ ROOT.
            if target.startswith("/"):
                dest = ROOT / target.lstrip("/")
            else:
                dest = (md.parent / target).resolve()
            if not dest.exists():
                errors.append(f"Link gãy trong {md.relative_to(ROOT)}: {target}")


def check_cyrillic(errors: list[str]) -> None:
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if CYRILLIC_RE.search(line):
                errors.append(f"Ký tự Cyrillic trong {md.relative_to(ROOT)}:{i}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    # Chương.
    present = 0
    for ch in CHAPTERS:
        readme = ROOT / "chapters" / ch / "README.md"
        if readme.exists():
            present += 1
        else:
            errors.append(f"Thiếu chương: chapters/{ch}/README.md")

    # Sidebar.
    sidebar = ROOT / "_sidebar.md"
    if sidebar.exists():
        sb = sidebar.read_text(encoding="utf-8")
        for ch in CHAPTERS:
            if f"chapters/{ch}/README.md" not in sb:
                errors.append(f"Sidebar thiếu chương: {ch}")
    else:
        errors.append("Thiếu _sidebar.md")

    # Resources / case-studies / community.
    for r in RESOURCES:
        if not (ROOT / "resources" / f"{r}.md").exists():
            errors.append(f"Thiếu resource: resources/{r}.md")
    for c in CASE_STUDIES:
        if not (ROOT / "case-studies" / f"{c}.md").exists():
            errors.append(f"Thiếu case study: case-studies/{c}.md")
    for c in COMMUNITY:
        if not (ROOT / "community" / f"{c}.md").exists():
            errors.append(f"Thiếu community: community/{c}.md")

    # .nojekyll rỗng.
    nojekyll = ROOT / ".nojekyll"
    if nojekyll.exists() and nojekyll.stat().st_size != 0:
        warnings.append(".nojekyll không rỗng")

    check_local_links(errors)
    check_cyrillic(errors)

    print(f"Chương: {present}/{len(CHAPTERS)}")
    print(f"Resource: {len(RESOURCES)} | Case study: {len(CASE_STUDIES)} | "
          f"Community: {len(COMMUNITY)}")
    for w in warnings:
        print(f"  [warning] {w}")
    if errors:
        print(f"\n{len(errors)} errors:")
        for e in errors:
            print(f"  [error] {e}")
        print("\nKẾT QUẢ: FAIL")
        return 1
    print(f"\nValidator: 0 errors, {len(warnings)} warnings")
    print("KẾT QUẢ: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

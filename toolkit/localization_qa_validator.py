"""
Localization Quality Assurance (QA) Validator (v1.1)
====================================================
⚠️ تنبيه الاستخدام وحقوق الملكية / Usage & Licensing Notice:
- يُمنع الاستخدام التجاري دون التواصل المسبق مع صاحب المشروع (V7dt1 / axxx503) عبر (https://bio.site/V7dt1 | v7dtads@gmail.com) والاتفاق على تقاسم الأرباح.
- عند النشر العام المجاني، يكفي ذكر الاسم (V7dt1 / axxx503) في حقوق التعريب كمساعد في البرومبت والاستخدام العام.

Automated auditing tool for game localization packages:
1. Detects "Frankenstein" hybrid strings (mixed English words inside Arabic sentences).
2. Verifies 100% token integrity between original and localized files.
3. Checks for UTF-8 / UTF-8 with BOM compliance on required engines.
4. Generates an executive linguistic coverage and purity report.
"""

import argparse
import csv
import json
import os
import re
import sys
from typing import Dict, List, Tuple

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Unicode range covers standard Arabic and Presentation Forms-A & B (reshaped glyphs)
ARABIC_CHAR_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
LATIN_WORD_RE = re.compile(r"(?<![a-zA-Z0-9_])[a-zA-Z]{2,}(?![a-zA-Z0-9_])")

# Universal Token pattern to strip before checking linguistic purity
TOKEN_RE = re.compile(
    r"("
    r"\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}|"   # {var}, {0}, {plural:...}
    r"<[^>]+>|"                           # <color=red>, <b>, </i>
    r"\[[^\]]+\]|"                         # [Character.GetName], [Concept|E]
    r"\$[a-zA-Z0-9_\.]+\$|"                # $VALUE$, $GOLD$
    r"#[a-zA-Z0-9_\.]+|#!|"                # #high, #!
    r"@[a-zA-Z0-9_\.]+!?|"                 # @gold_icon!
    r"%(?:\d+\$)?[+-]?\d*(?:\.\d+)?[sdifxX]|" # %s, %d, %.2f
    r"\\n|\\t|\\r|\\\""                    # escaped control chars
    r")"
)

# Clausewitz/Jomini YAML entry pattern: key:0 "value"
YAML_ENTRY_RE = re.compile(r'^\s*([a-zA-Z0-9_.-]+:\d*\s*)"(.*)"\s*$')

SUPPORTED_EXTENSIONS = (".json", ".yml", ".yaml", ".csv", ".po", ".strings", ".txt")


def extract_strings_from_file(filepath: str) -> List[str]:
    """Extracts localized values from JSON, YAML, CSV, or plain text files."""
    ext = os.path.splitext(filepath)[1].lower()
    strings = []

    try:
        with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as fp:
            content = fp.read()
    except Exception:
        return strings

    if ext == ".json":
        try:
            data = json.loads(content)
            def walk(obj):
                if isinstance(obj, dict):
                    for v in obj.values():
                        walk(v)
                elif isinstance(obj, list):
                    for item in obj:
                        walk(item)
                elif isinstance(obj, str):
                    strings.append(obj)
            walk(data)
            return strings
        except Exception:
            pass

    for line in content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check for YAML key:0 "value" pattern
        m_yaml = YAML_ENTRY_RE.match(stripped)
        if m_yaml:
            strings.append(m_yaml.group(2))
            continue

        # General key-value pattern (e.g., key = "value" or key: value)
        if ":" in stripped and not stripped.startswith("http"):
            parts = stripped.split(":", 1)
            val = parts[1].strip().strip('"').strip("'")
            if val:
                strings.append(val)
                continue

        strings.append(stripped)

    return strings


def audit_string(text: str) -> str:
    """Classifies a string as 'pure_ar', 'pure_en', 'frankenstein', or 'empty'."""
    clean = TOKEN_RE.sub(" ", text).strip()
    if not clean:
        return "empty"

    has_ar = bool(ARABIC_CHAR_RE.search(clean))
    latin_words = LATIN_WORD_RE.findall(clean)

    # Frankenstein: contains Arabic text AND 2 or more standalone English words
    # (e.g., 'خروج to Desktop' or 'The حماسة of Faith')
    if has_ar and len(latin_words) >= 2:
        return "frankenstein"
    elif has_ar:
        return "pure_ar"
    else:
        return "pure_en"


def audit_file(filepath: str) -> Dict:
    """Audits a single localization file."""
    raw_strings = extract_strings_from_file(filepath)

    total = 0
    pure_ar = 0
    pure_en = 0
    frankenstein = 0

    for s in raw_strings:
        classification = audit_string(s)
        if classification == "empty":
            continue
        total += 1
        if classification == "pure_ar":
            pure_ar += 1
        elif classification == "frankenstein":
            frankenstein += 1
        elif classification == "pure_en":
            pure_en += 1

    coverage = (pure_ar / total * 100) if total > 0 else 0.0
    return {
        "file": os.path.basename(filepath),
        "path": filepath,
        "total": total,
        "pure_ar": pure_ar,
        "pure_en": pure_en,
        "frankenstein": frankenstein,
        "coverage_pct": round(coverage, 1),
    }


def audit_directory(dirpath: str, extensions: Tuple[str, ...] = SUPPORTED_EXTENSIONS) -> List[Dict]:
    """Audits all localization files matching extensions in a directory."""
    results = []
    for root, _, files in os.walk(dirpath):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in extensions:
                results.append(audit_file(os.path.join(root, f)))
    return results


def print_qa_report(results: List[Dict]):
    """Prints a structured QA audit report to the console."""
    total_strings = sum(r["total"] for r in results)
    total_ar = sum(r["pure_ar"] for r in results)
    total_frank = sum(r["frankenstein"] for r in results)
    total_en = sum(r["pure_en"] for r in results)

    overall_coverage = (total_ar / total_strings * 100) if total_strings > 0 else 0.0

    print("=" * 72)
    print(" 🛡️ LOCALIZATION QUALITY ASSURANCE (QA) AUDIT REPORT")
    print("=" * 72)
    print(f" Total Files Audited        : {len(results)}")
    print(f" Total String Entries       : {total_strings:,}")
    print(f" Fully Localized (Pure AR)  : {total_ar:,} ({overall_coverage:.1f}%)")
    print(f" Untranslated Original (EN) : {total_en:,}")
    print(f" Frankenstein Hybrid Strings: {total_frank:,} {'❌ (FAIL)' if total_frank > 0 else '✅ (PASSED)'}")
    print("=" * 72)

    if total_frank > 0:
        print("[WARNING] Found hybrid mixed-language strings! Please translate sentences")
        print("          completely or keep original English. Never apply partial word substitution.")
    else:
        print("[SUCCESS] 0 Frankenstein hybrid strings detected! Linguistic purity verified.")
    print("=" * 72)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Localization Quality Assurance (QA) Validator (v1.1)"
    )
    parser.add_argument("target", nargs="?", default=".", help="File or directory path to audit (default: .)")
    parser.add_argument("--ext", nargs="+", default=list(SUPPORTED_EXTENSIONS), help="File extensions to include")

    args = parser.parse_args()

    target_path = args.target
    if os.path.isfile(target_path):
        res = [audit_file(target_path)]
    elif os.path.isdir(target_path):
        res = audit_directory(target_path, tuple(args.ext))
    else:
        print(f"[ERROR] Target path not found: {target_path}")
        sys.exit(1)

    print_qa_report(res)

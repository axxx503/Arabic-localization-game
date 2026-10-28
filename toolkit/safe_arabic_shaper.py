"""
Safe Arabic Reshaper & BiDi Pre-Processor for Game Localization (v1.1)
======================================================================
⚠️ تنبيه الاستخدام وحقوق الملكية / Usage & Licensing Notice:
- يُمنع الاستخدام التجاري دون التواصل المسبق مع صاحب المشروع (V7dt1 / axxx503) عبر (https://bio.site/V7dt1 | v7dtads@gmail.com) والاتفاق على تقاسم الأرباح.
- عند النشر العام المجاني، يكفي ذكر الاسم (V7dt1 / axxx503) في حقوق التعريب كمساعد في البرومبت والاستخدام العام.
- Commercial use is strictly prohibited without contacting the author (V7dt1 / axxx503) via https://bio.site/V7dt1 or v7dtads@gmail.com for a profit-sharing agreement. For free public releases, crediting (V7dt1 / axxx503) is sufficient.

Features in v1.1:
- Universal Token Protection: Preserves {...}, <...>, [...], $VAR$, #tag#!, @icon!, %s/%d format specifiers, and escapes.
- SmartFormat Plural Shaper: Shapes inner Arabic choices inside {var:plural:choice1|choice2}.
- Multi-Line Natural Wrapping: Wraps lines at word boundaries BEFORE BiDi to prevent inverted lines in LTR engines.
- Linguistic Purity Gate: Prevents BiDi corruption on mixed/predominantly Latin strings (Zero Frankenstein distortion).
"""

import re
import textwrap
import arabic_reshaper
from bidi.algorithm import get_display

RESHAPER = arabic_reshaper.ArabicReshaper(configuration={
    "delete_harakat": False,
    "support_ligatures": True,
})

# Universal token pattern matching all major engine placeholder syntax
TOKEN_RE = re.compile(
    r"("
    r"\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}|"   # {var}, {var:plural:...}, {0}
    r"<[^>]+>|"                           # <color=red>, <b>, </size>
    r"\[[^\]]+\]|"                         # [Character.GetName], [Concept|E], [b]
    r"\$[a-zA-Z0-9_\.]+\$|"                # $VALUE$, $WHEN$, $GOLD$
    r"#[a-zA-Z0-9_\.]+|#!|"                # #high, #weak, #P, #I, #!
    r"@[a-zA-Z0-9_\.]+!?|"                 # @gold_icon!, @warning_icon!
    r"%(?:\d+\$)?[+-]?\d*(?:\.\d+)?[sdifxX]|" # %s, %d, %1$s, %.2f
    r"\\n|\\t|\\r|\\\""                    # escaped control characters
    r")"
)

PLURAL_RE = re.compile(r"^\{([a-zA-Z0-9_]+):plural:([^|{}]+)\|([^{}]+)\}$")
ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
LATIN_RE = re.compile(r"[a-zA-Z]")


def shape_token_if_plural(tok: str) -> str:
    """Recursively shapes Arabic text inside SmartFormat plural expressions."""
    m = PLURAL_RE.match(tok)
    if not m:
        return tok
    var_name, c1, c2 = m.group(1), m.group(2), m.group(3)
    return f"{{{var_name}:plural:{shape_line(c1)}|{shape_line(c2)}}}"


def is_predominantly_arabic(clean_text: str) -> bool:
    """Linguistic Purity Gate: Ensures line is predominantly Arabic before applying RTL BiDi."""
    ar_count = len(ARABIC_RE.findall(clean_text))
    lat_count = len(LATIN_RE.findall(clean_text))
    if ar_count == 0:
        return False
    # If Latin letters strictly outnumber Arabic letters (e.g. Frankenstein text), reject RTL reversal
    if lat_count > ar_count * 1.5:
        return False
    return True


def shape_line(line: str) -> str:
    """Shapes a single line with token protection and linguistic purity gating."""
    if not line or not ARABIC_RE.search(line):
        return line

    tokens = []
    def repl(m):
        idx = len(tokens)
        tokens.append(shape_token_if_plural(m.group(0)))
        return chr(0x05D0 + (idx % 25))

    protected = TOKEN_RE.sub(repl, line)

    # Check linguistic purity: do not apply RTL reversal on predominantly Latin sentences
    clean_for_check = TOKEN_RE.sub("", line)
    if not is_predominantly_arabic(clean_for_check):
        # Only reshape the Arabic characters, do not flip line direction
        reshaped = RESHAPER.reshape(protected)
        for idx, tok in enumerate(tokens):
            reshaped = reshaped.replace(chr(0x05D0 + (idx % 25)), tok, 1)
        return reshaped

    reshaped = RESHAPER.reshape(protected)
    vis = get_display(reshaped, base_dir="R")
    for idx, tok in enumerate(tokens):
        vis = vis.replace(chr(0x05D0 + (idx % 25)), tok, 1)
    return vis


def shape_arabic_text(logical_text: str, wrap_width: int = 58) -> str:
    """Full-paragraph token-safe shaper with natural line wrapping for LTR engines."""
    if not logical_text or not ARABIC_RE.search(logical_text):
        return logical_text

    out_lines = []
    for raw_line in logical_text.split("\n"):
        stripped = raw_line.strip()
        if not stripped:
            out_lines.append("")
            continue

        tokens = []
        def tok_protect(m):
            idx = len(tokens)
            tokens.append(m.group(0))
            return f"__TOK{idx}__"

        temp = TOKEN_RE.sub(tok_protect, stripped)
        if len(stripped) > wrap_width and wrap_width > 0:
            wrapped = textwrap.wrap(temp, width=wrap_width, break_long_words=False, break_on_hyphens=False)
        else:
            wrapped = [temp]

        for wline in wrapped:
            for idx, tok in enumerate(tokens):
                wline = wline.replace(f"__TOK{idx}__", tok)
            out_lines.append(shape_line(wline))

    return "\n".join(out_lines)


if __name__ == "__main__":
    import argparse
    import sys

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        description="Safe Arabic Reshaper & BiDi Pre-Processor for Game Localization (v1.1)"
    )
    parser.add_argument("--text", "-t", type=str, help="Single text string to reshape")
    parser.add_argument("--file", "-f", type=str, help="Path to input text file to reshape")
    parser.add_argument("--out", "-o", type=str, help="Path to output shaped file (optional)")
    parser.add_argument("--wrap", "-w", type=int, default=58, help="Line wrap width (default: 58, 0 to disable)")

    args = parser.parse_args()

    if args.text:
        print(shape_arabic_text(args.text, wrap_width=args.wrap))
    elif args.file:
        with open(args.file, "r", encoding="utf-8-sig", errors="ignore") as fp:
            content = fp.read()
        shaped = shape_arabic_text(content, wrap_width=args.wrap)
        if args.out:
            with open(args.out, "w", encoding="utf-8-sig") as fp:
                fp.write(shaped)
            print(f"[SUCCESS] Wrote shaped output to: {args.out}")
        else:
            print(shaped)
    else:
        # Quick self-test demonstration
        demo_text = "حفظ اللعبة باسم autosave_exit"
        demo_tokens = "المستوى {0} يحتاج إلى <color=gold>{1}</color> عملة ذهبية"
        print("Safe Arabic Shaper v1.1 - Self Test:")
        print("Input 1 :", demo_text)
        print("Shaped 1:", shape_line(demo_text))
        print("Input 2 :", demo_tokens)
        print("Shaped 2:", shape_line(demo_tokens))
        print("\nUse --help for CLI arguments.")


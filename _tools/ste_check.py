#!/usr/bin/env python3
"""Mechanical clarity check for the ICM clarity stage.

Usage (from the workspace root):
  python _tools/ste_check.py stages/NN_clarity/output/draft.md [--audience machine|human]

Checks prose only: frontmatter, fenced code blocks, and headings are skipped.
Hard findings (fail): sentences over the word limit, non-approved words,
verb-in-noun patterns. Soft findings (warn, listed but never fail): possible
passive voice.

Writes check.md beside the input: first line "pass" or "fail: <why>",
then the findings. Exit codes: 0 pass, 1 fail, 2 missing input.
"""

import argparse
import re
import sys
from pathlib import Path

# Approved replacements. Keep in sync with references/ste-rules.md.
APPROVED = {
    "utilize": "use", "utilise": "use", "facilitate": "help",
    "commence": "start", "terminate": "stop", "discontinue": "stop",
    "prior to": "before", "in order to": "to", "subsequent to": "after",
    "in the event of": "if", "due to the fact that": "because",
    "at this point in time": "now", "sufficient": "enough",
    "obtain": "get", "require": "need", "necessitate": "need",
    "approximately": "about", "regarding": "about", "concerning": "about",
    "assist": "help", "attempt": "try", "demonstrate": "show",
    "indicate": "show", "determine": "find out", "employ": "use",
    "ensure": "make sure", "implement": "carry out", "initiate": "start",
    "methodology": "method", "notify": "tell", "portion": "part",
    "possess": "have", "purchase": "buy", "transmit": "send",
    "verify": "check", "remainder": "rest", "a number of": "several",
    "the majority of": "most", "whether or not": "whether",
}

MAX_WORDS = {"machine": 20, "human": 25}

WORD_RE = re.compile(r"[A-Za-z0-9'-]+")
VERB_NOUN_RE = re.compile(
    r"\b(?:make|perform|carry out|conduct|provide|do)\s+"
    r"(?:a|an|the)\s+(\w+)\s+(?:of|on|to|for)\b",
    re.I,
)
PASSIVE_RE = re.compile(
    r"\b(?:am|is|are|was|were|be|been|being)\s+\w+(?:ed|wn|nt|ne)\b", re.I
)


def visible_text(md: str) -> str:
    """Strip frontmatter, fenced code, and headings; keep prose and tables."""
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    md = re.sub(r"^\s*#.*$", " ", md, flags=re.M)
    md = re.sub(r"^\s*[-| :]+[-|]+\s*$", " ", md, flags=re.M)  # table rules
    return re.sub(r"\s+", " ", md).strip()


def check(path: Path, audience: str) -> tuple[list[str], list[str]]:
    """Return (hard_findings, soft_findings) for the file."""
    text = visible_text(path.read_text(encoding="utf-8"))
    low = text.lower()
    limit = MAX_WORDS[audience]
    hard, soft = [], []

    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    for i, sent in enumerate(sentences, 1):
        n = len(WORD_RE.findall(sent))
        if n > limit:
            hard.append(f"S{i}: {n} words (max {limit}): {sent[:70]}")

    for bad, good in APPROVED.items():
        if re.search(rf"\b{re.escape(bad)}\b", low):
            hard.append(f"word: '{bad}' -> '{good}'")

    for m in VERB_NOUN_RE.finditer(text):
        hard.append(f"verb-in-noun: '{m.group(0)}' -> use the verb")

    for m in PASSIVE_RE.finditer(text):
        soft.append(f"possible passive: '{m.group(0)}'")

    return hard, soft


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file", type=Path)
    ap.add_argument("--audience", choices=MAX_WORDS, default="machine")
    args = ap.parse_args()

    if not args.file.is_file():
        print(f"missing input: {args.file}", file=sys.stderr)
        return 2

    hard, soft = check(args.file, args.audience)
    check_path = args.file.parent / "check.md"

    if hard:
        kinds = []
        if any(r.startswith("S") for r in hard):
            kinds.append("long sentences")
        if any(r.startswith("word") for r in hard):
            kinds.append("non-approved words")
        if any(r.startswith("verb-in-noun") for r in hard):
            kinds.append("verb-in-noun patterns")
        first = f"fail: {len(hard)} findings ({', '.join(kinds)})"
    else:
        first = "pass"

    lines = [first] + [f"- {f}" for f in hard] + [
        f"- (warning) {w}" for w in soft
    ]
    check_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{args.file.name}: {first} -> {check_path}")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())

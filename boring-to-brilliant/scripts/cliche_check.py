#!/usr/bin/env python3
"""Cliché check for B2B copy.

Flags generic B2B phrases and gives the copy a "specificity score" out of 100.

Usage:
    python cliche_check.py "Our innovative solutions empower your team"
    python cliche_check.py --file draft.md
    cat draft.md | python cliche_check.py
"""
import argparse
import re
import sys

CLICHES = {
    "empty superlative": [
        "cutting-edge", "cutting edge", "state-of-the-art", "state of the art",
        "best-in-class", "best in class", "world-class", "world class",
        "industry-leading", "industry leading", "leading provider",
        "next-generation", "next generation", "revolutionary", "game-changing",
        "game changer", "groundbreaking", "unparalleled", "unmatched",
        "second to none", "premier",
    ],
    "vague verb": [
        "empower", "enable", "leverage", "unlock", "transform", "revolutionize",
        "streamline", "optimize", "maximize", "elevate", "harness", "unleash",
        "drive value", "drive growth",
    ],
    "filler noun": [
        "solutions", "synergy", "ecosystem", "paradigm", "value proposition",
        "best practices", "one-stop shop", "end-to-end", "holistic", "robust",
        "scalable", "seamless", "seamlessly", "turnkey",
    ],
    "hollow promise": [
        "innovative", "innovation", "high-quality", "high quality", "reliable",
        "trusted partner", "customer-centric", "passionate",
        "committed to excellence", "peace of mind", "the future of",
        "next level", "excited to announce", "sustainable future",
    ],
}

FIXES = {
    "empty superlative": "Replace with the measurable fact that makes it 'best' (a number, a test, a ranking with source).",
    "vague verb": "Say the actual action: what can the buyer now do, and how fast?",
    "filler noun": "Name the specific thing: product, feature, integration, time it takes.",
    "hollow promise": "Prove it: warranty, uptime, certification, customer result.",
}


def find_cliches(text):
    hits = []
    lower = text.lower()
    for category, phrases in CLICHES.items():
        for phrase in phrases:
            pattern = r"(?<![\w-])" + re.escape(phrase) + r"\w*"
            for m in re.finditer(pattern, lower):
                hits.append((m.start(), text[m.start():m.end()], category))
    # Drop hits contained inside a longer hit (e.g. "innovative" inside "innovative solutions" is fine to keep both,
    # but "cutting edge" inside "cutting-edge" duplicates)
    hits.sort(key=lambda h: (h[0], -len(h[1])))
    deduped, last_end = [], -1
    for start, phrase, cat in hits:
        if start >= last_end:
            deduped.append((start, phrase, cat))
            last_end = start + len(phrase)
    return deduped


def score(text, hits):
    words = max(len(re.findall(r"\w+", text)), 1)
    numbers = len(re.findall(r"\d", text))
    density = len(hits) / words * 100  # clichés per 100 words
    s = 100 - density * 12 + min(numbers, 5) * 2
    return max(0, min(100, round(s)))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("text", nargs="?", help="Copy to check")
    p.add_argument("--file", help="Read copy from a file")
    args = p.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        p.print_help()
        sys.exit(1)

    hits = find_cliches(text)
    s = score(text, hits)
    verdict = ("Brilliant: specific and concrete" if s >= 85 else
               "OK: a few generic spots" if s >= 65 else
               "Boring: reads like every other B2B site")

    print(f"Specificity score: {s}/100  ({verdict})")
    print(f"Clichés found: {len(hits)}")
    if hits:
        by_cat = {}
        for _, phrase, cat in hits:
            by_cat.setdefault(cat, []).append(phrase)
        for cat, phrases in by_cat.items():
            uniq = sorted(set(x.lower() for x in phrases))
            print(f"\n  [{cat}] {', '.join(uniq)}")
            print(f"    Fix: {FIXES[cat]}")
    if not re.search(r"\d", text):
        print("\n  No numbers at all. B2B buyers trust specifics; add at least one provable figure.")


if __name__ == "__main__":
    main()

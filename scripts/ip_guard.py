#!/usr/bin/env python3
"""
TSCWH IP Guard — trade secret scanner for tscwh-public commits.

Scans every staged .md file for forbidden implementation details per the
TSCWH three-tier architecture firewall. Exits non-zero to block the commit
if any violation is found.

Run standalone:  python scripts/ip_guard.py [--all]
  --all : scan every .md file in the repo (not just staged)
"""

import re
import subprocess
import sys

# ---------------------------------------------------------------------------
# FORBIDDEN PATTERNS
# Each entry: (regex_pattern, human_readable_label)
# Patterns are matched case-insensitively unless noted.
# ---------------------------------------------------------------------------
FORBIDDEN = [
    # Architecture internals
    (r'\btoroidal\b',               "toroidal (architecture name)"),
    (r'\btorus\b',                  "torus (architecture name)"),
    (r'\bstate ring\b',             "state ring (architecture term)"),
    (r'\bcircular buffer\b',        "circular buffer (implementation detail)"),
    (r'shared_memory\.SharedMemory','shared_memory.SharedMemory (Python API)'),
    (r'1 KiB',                      "1 KiB (buffer size detail)"),
    (r'12-bit fixed.point',         "12-bit fixed-point (enforcement internal)"),
    (r'40 ns\b',                    "40 ns (latency internal)"),
    (r'\bbitmask\b',                "bitmask (enforcement internal)"),

    # Libraries / tools
    (r'\bZ3\b',                     "Z3 (SMT solver name)"),
    (r'\bSMT solver\b',             "SMT solver"),
    (r'\bSentenceTransformer\b',    "SentenceTransformer (library name)"),
    (r'\bChromaDB\b',               "ChromaDB (library name)"),
    (r'all-MiniLM',                 "all-MiniLM (model name)"),

    # Algorithms
    (r'Bayesian Truth Serum',       "Bayesian Truth Serum (algorithm name)"),
    (r'\bPrelec\b',                 "Prelec (algorithm name)"),
    (r'\bLyapunov\b',               "Lyapunov (algorithm name)"),
    (r'\bdV/dt\b',                  "dV/dt (stability formula)"),

    # Internal agent names (specific internal codenames)
    (r'\bGuardian\b',               "Guardian (internal agent codename)"),
    (r'\bShepherd\b',               "Shepherd (internal agent codename)"),
    (r'\bScribe\b',                 "Scribe (internal agent codename)"),
    (r'\bPredictor\b',              "Predictor (internal agent codename)"),
    (r'\bAdvocate\b',               "Advocate (internal agent codename)"),
    (r'\bProsecutor\b',             "Prosecutor (internal agent codename)"),

    # API / crypto internals
    (r'\bCSPRNG\b',                 "CSPRNG (API internal)"),
    (r'\bHMAC-SHA256\b',            "HMAC-SHA256 (cryptographic detail)"),
    (r'Fibonacci routing',          "Fibonacci routing (API routing detail)"),

    # Internal flags / config keys
    (r'\bSKIP_HEAVY\b',             "SKIP_HEAVY (internal flag)"),
    (r'\bBASIN_DELTA_EPSILON\b',    "BASIN_DELTA_EPSILON (internal config)"),
    (r'\bPHI_MAJOR\b',              "PHI_MAJOR (internal config)"),

    # Codebase metrics (exact counts)
    (r'54,?854',                    "54,854 LOC (codebase metric)"),
    (r'49,?000 LOC',                "49,000 LOC (codebase metric)"),
    (r'121 (?:source )?modules',    "121 modules (codebase metric)"),
    (r'128 modules',                "128 modules (codebase metric)"),
    (r'109 tests',                  "109 tests (codebase metric)"),

    # Biblical / origin references
    (r'Daniel 2:34',                "Daniel 2:34 (origin reference)"),
    (r'stone cut without hands',    "stone cut without hands (origin reference)"),

    # Pipeline structure
    (r'10.stage pipeline',          "10-stage pipeline (pipeline detail)"),
    (r'Stage 10 LLM',               "Stage 10 LLM call detail"),

    # Architecture pattern names
    (r'hexagonal (?:architecture|compliance)', "hexagonal architecture/compliance (internal pattern)"),
    (r'Full hexagonal',             "Full hexagonal compliance (internal pattern)"),
]

# ---------------------------------------------------------------------------


def get_staged_md_files():
    """Return list of .md files staged for commit."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True
    )
    return [f for f in result.stdout.splitlines() if f.endswith(".md")]


def get_all_md_files():
    """Return all tracked .md files in the repo."""
    result = subprocess.run(
        ["git", "ls-files", "*.md"],
        capture_output=True, text=True
    )
    return result.stdout.splitlines()


def scan_file(filepath):
    """Return list of (line_number, line_text, label) violations."""
    violations = []
    try:
        with open(filepath, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                for pattern, label in FORBIDDEN:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append((lineno, line.rstrip(), label))
                        break  # one violation per line is enough
    except FileNotFoundError:
        pass
    return violations


def main():
    scan_all = "--all" in sys.argv

    files = get_all_md_files() if scan_all else get_staged_md_files()

    if not files:
        if not scan_all:
            print("[ip-guard] No staged .md files to check.")
        return 0

    mode = "full repo" if scan_all else "staged"
    print(f"[ip-guard] Scanning {len(files)} {mode} .md file(s) for trade secrets...")

    total_violations = 0
    for filepath in files:
        violations = scan_file(filepath)
        if violations:
            total_violations += len(violations)
            print(f"\n  VIOLATION in {filepath}:")
            for lineno, text, label in violations:
                print(f"    line {lineno}: [{label}]")
                print(f"      > {text[:120]}")

    if total_violations:
        print(f"\n[ip-guard] BLOCKED — {total_violations} trade secret violation(s) found.")
        print("[ip-guard] Fix the violations above, then retry your commit.")
        return 1

    print(f"[ip-guard] Clean — no trade secret violations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

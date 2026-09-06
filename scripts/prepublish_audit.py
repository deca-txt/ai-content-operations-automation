#!/usr/bin/env python3

from pathlib import Path
import re
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()

SKIP_DIRS = {".git", "__pycache__"}

BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp",
    ".pdf", ".zip", ".sqlite", ".db", ".woff", ".woff2"
}

PATTERNS = [
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("bearer_token", re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{20,}", re.I)),
    ("google_api_key", re.compile(r"AIza[0-9A-Za-z\-_]{30,}")),
    ("github_token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("generic_secret_assignment", re.compile(
        r"(?i)\b(api[_-]?key|access[_-]?token|client[_-]?secret|password)\b\s*[:=]\s*[\"']?[^\"'\s]{12,}"
    )),
    ("localhost_prod_reference", re.compile(r"https?://(?:127\.0\.0\.1|localhost)(?::\d+)?/")),
]

SUSPICIOUS_FILENAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "credentials.json",
    "database.sqlite",
    "database.sqlite-wal",
    "database.sqlite-shm",
}

findings = []

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    if any(part in SKIP_DIRS for part in path.parts):
        continue

    rel = path.relative_to(ROOT)

    if path.name in SUSPICIOUS_FILENAMES:
        findings.append(("suspicious_file", str(rel), "filename"))
        continue

    if path.suffix.lower() in BINARY_EXTS:
        continue

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    for label, pattern in PATTERNS:
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append((label, str(rel), f"line {line}"))

if findings:
    print("PREPUBLISH_AUDIT=REVIEW_REQUIRED")
    for label, path, location in findings:
        print(f"{label}\t{path}\t{location}")
    sys.exit(2)

print("PREPUBLISH_AUDIT=PASS")

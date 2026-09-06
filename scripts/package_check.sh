#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="${1:-.}"

required=(
  README.md
  SANITIZATION.md
  SECURITY.md
  PUBLISHING_CHECKLIST.md
  LICENSE_NOTICE.md
  docs/index.md
  docs/architecture.md
  docs/workflows.md
  docs/data-model.md
  docs/reliability.md
  docs/timeline.md
  docs/learning-roadmap.md
  docs/future-roadmap.md
)

for file in "${required[@]}"; do
  [ -s "$ROOT/$file" ] || {
    echo "MISSING=$file"
    exit 1
  }
done

python3 "$ROOT/scripts/prepublish_audit.py" "$ROOT"

echo "PACKAGE_CHECK=PASS"

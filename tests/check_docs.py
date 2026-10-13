"""Validate relative Markdown targets, metadata consistency and required release files."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
meta = json.loads((root / "project.json").read_text(encoding="utf-8"))
errors = []
checked = 0
for file in root.rglob("*.md"):
    content = file.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if "://" in target or target.startswith("#"):
            continue
        path = target.split("#")[0]
        checked += 1
        if not (file.parent / path).exists():
            errors.append(f"missing target: {file.relative_to(root)} -> {path}")
for name in ("README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
             "docs/08-review.md", "evidence/offline-results.json"):
    if not (root / name).is_file():
        errors.append(f"missing required file: {name}")
for name in ("README.md", "CHANGELOG.md", "docs/release-notes.md", "docs/01-core.md"):
    if meta["version"] not in (root / name).read_text(encoding="utf-8"):
        errors.append(f"version mismatch: {name}")
if meta["brand"] not in (root / "README.md").read_text(encoding="utf-8"):
    errors.append("brand mismatch")
print(json.dumps({"relative_links_checked": checked, "errors": errors,
                  "passed": not errors}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))


"""Check local documentation links, query hashes, and walkthrough coverage."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")
FENCE = re.compile(r"^```.*?^```[^\n]*$", re.MULTILINE | re.DOTALL)


def heading_ids(text: str) -> set[str]:
    seen: dict[str, int] = {}
    anchors: set[str] = set()
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        base = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = seen.get(base, 0)
        seen[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def main() -> int:
    errors: list[str] = []
    documents = sorted(ROOT.rglob("*.md"))
    documents = [p for p in documents if ".git" not in p.parts]
    checked_links = 0

    for document in documents:
        text = FENCE.sub("", document.read_text(encoding="utf-8"))
        for raw_target in LINK.findall(text):
            target = urlsplit(raw_target.strip("<>"))
            if target.scheme or target.netloc:
                continue
            checked_links += 1
            destination = document.parent / unquote(target.path) if target.path else document
            destination = destination.resolve()
            if not destination.is_relative_to(ROOT):
                errors.append(f"{document.relative_to(ROOT)}: link leaves repository: {raw_target}")
            elif not destination.exists():
                errors.append(f"{document.relative_to(ROOT)}: missing link: {raw_target}")
            elif target.fragment and destination.suffix.lower() == ".md":
                body = FENCE.sub("", destination.read_text(encoding="utf-8"))
                if unquote(target.fragment) not in heading_ids(body):
                    errors.append(f"{document.relative_to(ROOT)}: missing heading: {raw_target}")

    provenance = json.loads((ROOT / "PROVENANCE.json").read_text(encoding="utf-8"))
    for entry in provenance:
        query = ROOT / entry["query"]
        if not query.is_file():
            errors.append(f"Missing query: {entry['query']}")
        elif hashlib.sha256(query.read_bytes()).hexdigest() != entry["sha256"]:
            errors.append(f"Query hash differs from provenance: {entry['query']}")

    catalog_root = ROOT / "docs" / "zimmerman"
    catalog = json.loads((catalog_root / "catalog.json").read_text(encoding="utf-8"))
    expected = {tool["walkthrough"] for tool in catalog["tools"]}
    actual = {
        path.relative_to(catalog_root).as_posix()
        for path in (catalog_root / "walkthroughs").glob("*.md")
    }
    if len(expected) != len(catalog["tools"]):
        errors.append("Duplicate walkthrough path in Zimmerman catalog")
    if expected != actual:
        errors.append(f"Walkthrough coverage differs: missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")

    fixture_root = ROOT / "examples" / "ez-csv-summary"
    summary = json.loads((fixture_root / "summary.json").read_text(encoding="utf-8"))
    fixture = (fixture_root / "synthetic-events.csv").read_bytes()
    if hashlib.sha256(fixture).hexdigest() != summary["input"]["sha256"]:
        errors.append("Synthetic CSV hash differs from stored summary")
    if len(fixture) != summary["input"]["size_bytes"]:
        errors.append("Synthetic CSV size differs from stored summary")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(
        f"Checked {len(documents)} Markdown files, {checked_links} local links, "
        f"{len(provenance)} query hashes, {len(actual)} walkthroughs, and the CSV fixture."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

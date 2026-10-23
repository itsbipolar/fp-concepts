"""Read one embedded kit file without installing its instructions or tools.

Usage: python3 scripts/read_motion_kit.py --list
       python3 scripts/read_motion_kit.py .claude/skills/motion-graphic/references/SOUND.md
       python3 scripts/read_motion_kit.py --verify
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "vendor/motion-kit/PAPER-COLLAGE-MOTION-KIT.md"
EXPECTED = "c7bbbd7ef924931b6aae24e6ae189f2c5c9317dc2764632af25fcae317337aea"


def inventory():
    data = ARCHIVE.read_bytes()
    if hashlib.sha256(data).hexdigest() != EXPECTED:
        raise ValueError("Supplied kit changed; review provenance before updating the pinned hash")
    lines = data.decode("utf-8").splitlines(keepends=True)
    files = {}
    i = 0
    while i < len(lines):
        match = re.fullmatch(r"<!-- FILE: (.+?) -->\r?\n?", lines[i])
        if not match:
            i += 1
            continue
        name = match[1]
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name or name in files:
            raise ValueError(f"Unsafe or duplicate embedded path: {name}")
        marker = i + 1
        i += 1
        fence = re.match(r"^(`{3,})[^`]*\r?\n?$", lines[i]) if i < len(lines) else None
        if not fence:
            raise ValueError(f"Missing opening fence: {name}")
        closing = fence[1]
        start = i + 1
        i = start
        while i < len(lines) and lines[i].strip() != closing:
            i += 1
        if i == len(lines):
            raise ValueError(f"Unclosed embedded file: {name}")
        content = "".join(lines[start:i])
        files[name] = {"path": name, "marker_line": marker, "content_start_line": start + 1,
                       "content_end_line": i, "sha256": hashlib.sha256(content.encode()).hexdigest(),
                       "content": content}
        i += 1
    if len(files) != 44:
        raise ValueError(f"Expected 44 embedded files; found {len(files)}")
    return files


def main():
    files = inventory()
    argument = sys.argv[1] if len(sys.argv) == 2 else "--list"
    if argument == "--verify":
        index = json.loads((ROOT / "vendor/motion-kit/index.json").read_text())
        actual = [{k: v for k, v in entry.items() if k != "content"} for entry in files.values()]
        if index["files"] != actual or index["archive_sha256"] != EXPECTED:
            raise ValueError("Kit index differs from the original archive")
        print("Motion kit OK: original SHA-256 and all 44 indexed text blocks verified.")
    elif argument == "--list":
        for name, entry in files.items():
            print(f"{entry['marker_line']:4}  {name}")
    elif argument in files:
        sys.stdout.write(files[argument]["content"])
    else:
        raise ValueError("Use --list, --verify, or an exact embedded file path; this reader never installs files")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        sys.exit(str(error))

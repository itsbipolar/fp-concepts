"""Validate the portable visual kit using only the Python standard library.

Run from any directory. This checks integrity and wiring, not visual quality.
"""
from pathlib import Path
import hashlib
import json
import re
import struct
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", "CLAUDE.md", "README.md",
    ".agents/skills/fp-visual-build/SKILL.md",
    "docs/PROJECT-STATE.md", "docs/STYLE-SYSTEM.md",
    "docs/BUILD-WORKFLOW.md", "docs/INTERACTION-PRINCIPLES.md",
    "docs/templates/LESSON-BRIEF.md", "docs/templates/IMAGE-PROMPT.md",
    "docs/templates/AGENT-TASK.md", "docs/templates/ASSET-RECORD.json",
    ".agents/skills/fp-video-build/SKILL.md", "docs/VIDEO-DIRECTION.md",
    "docs/VIDEO-WORKFLOW.md", "docs/templates/VIDEO-BRIEF.md",
    "vendor/motion-kit/README.md", "video/README.md", "video/BRIEF.md",
    "docs/VIDEO-EDITORIAL.md", "docs/VIDEO-EVIDENCE.md",
    "docs/templates/VIDEO-SCRIPT.md", "docs/templates/VIDEO-CLAIMS.json",
    "docs/templates/VIDEO-DELIVERY.json", "reference/vox-videos/README.md",
    "video/editorial/README.md",
    "video/projects/salary-dividend/README.md",
    "video/projects/salary-dividend/BRIEF.md",
    "video/projects/salary-dividend/SCRIPT.md",
    "video/projects/salary-dividend/STORYBOARD.md",
)


def checked_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Path outside repository: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing file: {relative}")
    return path


def validate():
    for name in REQUIRED:
        checked_path(name)
    manifest = json.loads(checked_path("design/within-reach/asset-manifest.json").read_text())
    tokens = json.loads(checked_path("design/within-reach/style-tokens.json").read_text())
    json.loads(checked_path("docs/templates/ASSET-RECORD.json").read_text())
    if manifest["schema_version"] != 1 or tokens["schema_version"] != 1:
        raise ValueError("Unsupported visual kit schema")
    if manifest["style_id"] != tokens["style_id"]:
        raise ValueError("Manifest and token style IDs differ")

    assets = manifest["assets"]
    ids = [asset["id"] for asset in assets]
    expected = {"within-reach-master", "within-reach-company", "within-reach-owner",
                "within-reach-payment", "colossus-master", "separate-bodies-master"}
    if len(ids) != len(set(ids)) or not expected.issubset(ids):
        raise ValueError("Missing or duplicate canonical asset IDs")
    for asset in assets:
        data = checked_path(asset["path"]).read_bytes()
        if hashlib.sha256(data).hexdigest() != asset["sha256"]:
            raise ValueError(f"Protected image changed: {asset['path']}")
        if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
            raise ValueError(f"Not a PNG with an IHDR header: {asset['path']}")
        width, height, _, colour_type = struct.unpack(">IIBB", data[16:26])
        if [width, height] != asset["dimensions_px"] or len(data) != asset["bytes"]:
            raise ValueError(f"Image dimensions/size mismatch: {asset['path']}")
        if (colour_type in (4, 6)) != asset["has_alpha_channel"]:
            raise ValueError(f"Alpha-channel metadata mismatch: {asset['path']}")

    video_references = json.loads(checked_path("design/within-reach/video-reference-manifest.json").read_text())
    if video_references["style_id"] != manifest["style_id"]:
        raise ValueError("Video direction differs from the approved style")
    for reference in video_references["references"]:
        if hashlib.sha256(checked_path(reference["path"]).read_bytes()).hexdigest() != reference["sha256"]:
            raise ValueError(f"Video reference changed: {reference['path']}")

    imported = json.loads(checked_path("reference/vox-videos/manifest.json").read_text())
    for entry in imported["files"]:
        source = checked_path("reference/vox-videos/" + entry["local_path"])
        if not source.is_relative_to(ROOT / "reference/vox-videos/source"):
            raise ValueError("Imported reference must stay inside its source archive")
        if hashlib.sha256(source.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError(f"Imported source changed: {entry['local_path']}")
    topics = json.loads(checked_path("video/editorial/topic-bank.json").read_text())["ideas"]
    topic_ids = [topic["id"] for topic in topics]
    if len(topic_ids) != len(set(topic_ids)):
        raise ValueError("Duplicate editorial topic IDs")
    for topic in topics:
        if topic["source"]["commit"] != imported["commit"] or topic["source"]["id"] != topic["id"]:
            raise ValueError(f"Topic provenance differs from reviewed source: {topic['id']}")
    for name in ("VIDEO-CLAIMS", "VIDEO-DELIVERY"):
        template = json.loads(checked_path(f"docs/templates/{name}.json").read_text())
        if template["schema_version"] != 1:
            raise ValueError(f"Unknown template schema: {name}")
    json.loads(checked_path("video/editorial/cast.json").read_text())

    # Tokens describe the actual approved prototype, not an invented new theme.
    prototype = checked_path("explorations/within-reach/index.html").read_text()
    for colour in tokens["colors"].values():
        if not re.fullmatch(r"#[0-9a-fA-F]{6}", colour["hex"]):
            raise ValueError(f"Invalid colour anchor: {colour['hex']}")
        pattern = re.escape(colour["css_variable"]) + r"\s*:\s*" + re.escape(colour["hex"]) + r"(?=[;}\s])"
        if not re.search(pattern, prototype, re.I):
            raise ValueError(f"Colour anchor differs from prototype: {colour['css_variable']}")

    # Check local Markdown destinations in the entry points; remote URLs are not fetched.
    for name in REQUIRED:
        if not name.endswith(".md"):
            continue
        source = checked_path(name)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", source.read_text()):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (source.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                raise ValueError(f"Broken local link in {name}: {target}")

    print(f"Visual kit OK: {len(assets)} protected PNGs, {len(tokens['colors'])} palette anchors.")
    print(f"Video continuity: {len(video_references['references'])} reference hashes verified.")
    print(f"Editorial transfer: {len(imported['files'])} source hashes and {len(topics)} topic provenance records verified.")
    print("Startup documents, templates and local Markdown links resolve.")
    print("Integrity only: visual fidelity and financial correctness require their own review.")


if __name__ == "__main__":
    try:
        validate()
    except (OSError, ValueError, KeyError, TypeError, struct.error) as error:
        print(f"Visual kit check failed: {error}", file=sys.stderr)
        sys.exit(1)

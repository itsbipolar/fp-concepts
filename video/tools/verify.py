"""Verify the actual rendered artifacts and build a contact sheet; standard library + FFmpeg."""
from pathlib import Path
import hashlib
import json
import struct
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "review"


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((REVIEW / "render-manifest.json").read_text())
    for name, expected in manifest["inputs"].items():
        assert sha(ROOT / name) == expected, f"Render source changed: {name}; run npm run render"
    for name, expected in manifest["artifacts"].items():
        assert sha(REVIEW / name) == expected, f"Rendered artifact changed: {name}; run npm run render"
    for asset in json.loads((ROOT / "asset-manifest.json").read_text())["assets"]:
        assert sha(ROOT.parent / asset["source"]) == asset["sha256"], f"Changed source asset: {asset['id']}"
        assert sha(ROOT / "public/assets" / asset["file"]) == asset["sha256"], f"Changed prepared asset: {asset['id']}"
    for frame in [0, 66, 108, 156, 210, 269]:
        data = (REVIEW / f"frame-{frame:03}.png").read_bytes()
        assert data[:8] == b"\x89PNG\r\n\x1a\n"
        assert struct.unpack(">II", data[16:24]) == (1280, 720)
    assert sha(REVIEW / "frame-210.png") == sha(REVIEW / "frame-269.png"), "Final composition should hold still"
    movie = REVIEW / "within-reach-motion-study.mp4"
    probe = json.loads(run("ffprobe", "-v", "error", "-count_frames", "-show_streams", "-show_format", "-of", "json", str(movie)))
    streams = probe["streams"]
    assert len(streams) == 1 and streams[0]["codec_type"] == "video", "Study should be silent"
    stream = streams[0]
    assert (stream["width"], stream["height"]) == (1280, 720)
    # FFmpeg reports full-range 4:2:0 as yuvj420p even when yuv420p was requested.
    assert stream["codec_name"] == "h264" and stream["pix_fmt"] in ("yuv420p", "yuvj420p")
    assert stream["r_frame_rate"] == "30/1" and int(stream["nb_read_frames"]) == 270
    assert abs(float(probe["format"]["duration"]) - 9) < 0.01
    run("ffmpeg", "-v", "error", "-xerror", "-i", str(movie), "-f", "null", "-")
    run("ffmpeg", "-v", "error", "-y", "-pattern_type", "glob", "-i", str(REVIEW / "frame-*.png"),
        "-vf", "scale=480:270,tile=3x2:padding=12:margin=12:color=0xfff9d8", "-frames:v", "1", str(REVIEW / "contact-sheet.png"))
    result = {
        "checks_passed": ["render inputs and output hashes", "four source/prepared asset hashes", "six 1280x720 stills",
                          "identical settled frames at 7s and 8.97s", "H.264 4:2:0 1280x720 30fps 270 frames / 9 seconds",
                          "silent video stream", "complete FFmpeg decode"],
        "movie_bytes": movie.stat().st_size,
        "pixel_format": stream["pix_fmt"],
        "scope": "Artifact integrity/render checks. Not a TypeScript typecheck, visual approval or financial verification.",
    }
    (REVIEW / "validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

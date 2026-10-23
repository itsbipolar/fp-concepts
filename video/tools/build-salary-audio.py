"""Build the 14s draft soundtrack from the user's existing generated narration.

python3 tools/build-salary-audio.py --source /path/to/source-voice.wav
No synthesis API, downloaded sound samples or optional Python dependencies.
"""
from array import array
import argparse
import hashlib
import json
import math
from pathlib import Path
import random
import sys
import wave

VIDEO = Path(__file__).resolve().parents[1]
PROJECT = VIDEO / "projects/salary-dividend"
EXPECTED = "b873d8cfb1bb447beac51728207c5f2e40562200c89d492c3e96a7f6d6f20982"
RATE = 48000
DURATION = 14


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    args = parser.parse_args()
    original = args.source.read_bytes()
    if hashlib.sha256(original).hexdigest() != EXPECTED:
        raise ValueError("Narration differs from the reviewed upstream recording")
    with wave.open(str(args.source)) as source:
        if (source.getframerate(), source.getnchannels(), source.getsampwidth()) != (RATE, 2, 2):
            raise ValueError("Expected original 48kHz stereo 16-bit PCM")
        samples = array("h", source.readframes(source.getnframes()))
    if sys.byteorder != "little":
        samples.byteswap()
    selections = [
        {"source_start": 16.51, "source_end": 19.56, "target_start": 3.25,
         "spoken_start": 3.3, "spoken_end": 6.16,
         "text": "Take it as a dividend, and the company pays its tax first."},
        {"source_start": 19.73, "source_end": 22.94, "target_start": 8.25,
         "spoken_start": 8.3, "spoken_end": 11.3,
         "text": "You get a tax break for that, but you still pay tax on the rest."},
    ]
    mixed = [0.0] * (DURATION * RATE)
    for edit in selections:
        a, b = round(edit["source_start"] * RATE), round(edit["source_end"] * RATE)
        at = round(edit["target_start"] * RATE)
        for index, frame in enumerate(range(a, b)):
            fade = min(1, index / 240, (b - a - index - 1) / 240)
            mono = (samples[2 * frame] + samples[2 * frame + 1]) / 65536
            mixed[at + index] += mono * max(0, fade) * 1.5

    # Restrained, newly generated paper contact: seeded noise through a simple
    # high-pass/low-pass pair, soft envelope, no whoosh or musical bed.
    cues = [(2.5, 0.18, 0.026), (4.2, 0.26, 0.022), (10.2, 0.12, 0.032)]
    for seed, (start, duration, volume) in enumerate(cues, 710):
        rng = random.Random(seed)
        low, previous = 0.0, 0.0
        length = round(duration * RATE)
        for index in range(length):
            noise = rng.uniform(-1, 1)
            low += 0.38 * (noise - low)
            high = low - previous
            previous += 0.045 * (low - previous)
            envelope = math.sin(math.pi * index / length) ** 1.4
            mixed[round(start * RATE) + index] += high * envelope * volume
    peak = max(abs(value) for value in mixed)
    gain = min(1.0, 0.82 / peak) if peak else 1
    pcm = array("h", (round(max(-1, min(1, value * gain)) * 32767) for value in mixed))
    if sys.byteorder != "little":
        pcm.byteswap()
    audio_dir = PROJECT / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    output = audio_dir / "passage.wav"
    with wave.open(str(output), "wb") as target:
        target.setnchannels(1)
        target.setsampwidth(2)
        target.setframerate(RATE)
        target.writeframes(pcm.tobytes())
    runtime = VIDEO / "public/assets/salary-dividend-passage.wav"
    runtime.parent.mkdir(parents=True, exist_ok=True)
    runtime.write_bytes(output.read_bytes())
    provenance = {
        "source_repository": "https://github.com/itsbipolar/fp-canada-vox-videos",
        "source_commit": "7eee559f25f1f974b3fcd094814852b331d32610",
        "source_path": "public/graphics/salary-vs-dividend/voice.wav",
        "source_sha256": EXPECTED,
        "upstream_provider_metadata": {"provider": "Higgsfield", "model": "seed_audio", "preset": "Benji"},
        "disclosure": "AI-generated narration reused from the user's previous project; no new synthesis call.",
        "edits": selections,
        "processing": "Two intact phrases, silent spacing, 5ms edge fades, stereo averaged to mono, 1.5x voice gain. No speed/pitch change.",
        "paper_sound_cues": [{"start": t, "duration": d, "amplitude": a} for t, d, a in cues],
        "duration_seconds": DURATION,
        "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "output_sample_peak_dbfs": round(20 * math.log10(peak * gain), 2),
        "new_voice_calls": 0,
    }
    (audio_dir / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps({"output": str(output), "duration": DURATION,
                      "sample_peak_dbfs": provenance["output_sample_peak_dbfs"]}, indent=2))


if __name__ == "__main__":
    main()

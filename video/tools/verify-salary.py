"""Verify passage artifacts using Python standard library and FFmpeg."""
from pathlib import Path
import hashlib
import json
import struct
import subprocess
ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / 'projects/salary-dividend/review'
def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    manifest = json.loads((REVIEW / 'render-manifest.json').read_text())
    for name, expected in manifest['inputs'].items():
        assert sha(ROOT / name) == expected, f'Render input changed: {name}'
    for name, expected in manifest['artifacts'].items():
        assert sha(REVIEW / name) == expected, f'Artifact changed: {name}'
    for asset in json.loads((ROOT / 'asset-manifest.json').read_text())['assets']:
        assert sha(ROOT.parent / asset['source']) == asset['sha256']
        assert sha(ROOT / 'public/assets' / asset['file']) == asset['sha256']
    assert sha(ROOT / 'projects/salary-dividend/audio/passage.wav') == sha(ROOT / 'public/assets/salary-dividend-passage.wav')
    for frame in [57, 78, 125, 156, 204, 249, 300, 359, 419]:
        data = (REVIEW / f'frame-{frame:03}.png').read_bytes()
        assert data[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', data[16:24]) == (1280, 720)
    assert sha(REVIEW / 'frame-359.png') == sha(REVIEW / 'frame-419.png')
    movie = REVIEW / 'salary-dividend-passage.mp4'
    probe = json.loads(run('ffprobe', '-v', 'error', '-count_frames', '-show_streams', '-show_format', '-of', 'json', str(movie)))
    video = [s for s in probe['streams'] if s['codec_type'] == 'video']
    audio = [s for s in probe['streams'] if s['codec_type'] == 'audio']
    assert len(video) == 1 and len(audio) == 1
    stream = video[0]
    assert (stream['width'], stream['height']) == (1280, 720)
    assert stream['codec_name'] == 'h264' and stream['pix_fmt'] in ('yuv420p', 'yuvj420p')
    assert stream['r_frame_rate'] == '30/1' and int(stream['nb_read_frames']) == 420
    assert abs(float(probe['format']['duration']) - 14) < .02
    assert audio[0]['codec_name'] == 'aac' and audio[0]['sample_rate'] == '48000'
    run('ffmpeg', '-v', 'error', '-xerror', '-i', str(movie), '-f', 'null', '-')
    hashes = run('ffmpeg', '-v', 'error', '-i', str(movie), '-vf', 'select=gte(n\\,359)', '-an', '-f', 'framemd5', '-')
    decoded = [line.split(',')[-1].strip() for line in hashes.splitlines() if line and not line.startswith('#')]
    assert len(decoded) == 61
    drift_path = REVIEW / 'decoded-hold-drift.txt'
    run('ffmpeg', '-v', 'error', '-i', str(movie), '-vf', 'select=gte(n\\,359),tblend=all_mode=difference,signalstats,metadata=print:file=' + str(drift_path), '-an', '-f', 'null', '-')
    lines = drift_path.read_text().splitlines()
    drift = {}
    for key in ['YMAX', 'YAVG', 'UMAX', 'VMAX']:
        values = [float(line.split('=')[1]) for line in lines if line.startswith('lavfi.signalstats.' + key + '=')]
        drift[key] = max(values)
    assert drift['YMAX'] <= 8 and drift['YAVG'] <= .01 and drift['UMAX'] <= 3 and drift['VMAX'] <= 3, 'Unexpected decoded static-hold drift'
    result = {'checks_passed': ['source/input/output SHA256 hashes', 'four preserved source/prepared assets', 'nine 1280x720 PNGs and contact sheet', 'byte-identical source hold frames359/419;61 decoded hold frames with bounded lossy drift', 'H264 4:2:0 1280x720 30fps 420 frames / 14 seconds', 'AAC 48kHz audio', 'complete FFmpeg audio/video decode'], 'movie_bytes': movie.stat().st_size, 'pixel_format': stream['pix_fmt'], 'decoded_hold_max_adjacent_difference': drift, 'scope': 'Artifact checks only. Not TypeScript typechecking, user approval or financial verification.'}
    (REVIEW / 'validation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()

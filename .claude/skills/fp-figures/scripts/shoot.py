#!/usr/bin/env python3
"""Render a built FP figure with headless Chrome: checks for review, stills and turntable clips for marketing.

    python3 shoot.py verify  OUT.html shots/            # every angle, closed and see-through, plus a phone shot
    python3 shoot.py press   OUT.html shots/ "Add RRIF@300,Withdraw@1500" [ms ...]   # a ?press= run at a few time budgets
    python3 shoot.py errors  OUT.html ["Add RRIF@300"] [query]   # script errors, NaN, the stats and window.__st
    python3 shoot.py social  OUT.html shots/ [query]    # clean stills: 1080x1350 (feed), 1080x1080 (square), 1920x1080 (wide)
    python3 shoot.py spin    OUT.html shots/ [query]    # 48-frame turntable -> spin.mp4 and spin.gif (needs ffmpeg)

query is extra URL parameters, e.g. "xr=1&labels=1&income=120000". Chrome is found from $CHROME, Playwright's
/opt/pw-browsers/chromium, google-chrome / chromium on PATH, or the macOS app. When Node + Playwright are installed,
all shots of a run go through one Playwright browser (real-time waits; the Chrome CLI's virtual time can hang while a
figure animates), otherwise each shot is its own Chrome CLI run with its own profile dir.
"""
import json, os, re, shutil, subprocess, sys, tempfile

def chrome():
    for c in [os.environ.get('CHROME'), '/opt/pw-browsers/chromium', shutil.which('google-chrome'), shutil.which('chromium'),
              shutil.which('chromium-browser'), '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']:
        if c and os.path.exists(c): return c
    sys.exit('no Chrome found: set $CHROME')

def run(page, query, out=None, size=(900, 800), scale=2, budget=3000, dump=False):
    url = 'file://' + os.path.abspath(page) + ('?' + query if query else '')
    prof = tempfile.mkdtemp(prefix='fpshot-')
    args = [chrome(), '--headless=new', '--hide-scrollbars', f'--user-data-dir={prof}', f'--force-device-scale-factor={scale}',
            f'--window-size={size[0]},{size[1]}', f'--virtual-time-budget={budget}']
    if hasattr(os, 'geteuid') and os.geteuid() == 0: args.append('--no-sandbox')   # containers run as root
    args += ['--dump-dom', url] if dump else [f'--screenshot={out}', url]
    r = subprocess.run(args, capture_output=True, text=True, timeout=300)
    shutil.rmtree(prof, ignore_errors=True)
    return r.stdout

PW_JS = r"""
const { chromium } = require('playwright');
(async () => {
  const [url, wait] = process.argv.slice(1);
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  const pg = await b.newPage({ viewport: { width: 900, height: 800 } });
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto(url); await pg.waitForTimeout(+wait);
  const r = await pg.evaluate(() => ({
    dataErrors: document.documentElement.dataset.errors || '',
    nan: /\bNaN\b/.test((document.getElementById('art') || {}).innerHTML || ''),
    stats: [...document.querySelectorAll('.stat')].map(s => s.innerText.replace(/\s+/g, ' ').trim()),
    state: JSON.stringify(window.__st, (k, v) => typeof v === 'number' ? Math.round(v * 100) / 100 : v) }));
  console.log('errors:', [...errs, r.dataErrors.trim()].filter(Boolean).join(' | ') || 'none');
  console.log('NaN in drawing:', r.nan); console.log('stats:', r.stats.join(' / ') || '-'); console.log('state:', r.state);
  await b.close();
})().catch(e => { console.error(e.message); process.exit(2); });
"""

def playwright_check(page, query, wait=4000):
    """Load the page in Playwright (Node) if it is installed: errors, NaN, the stats panel and window.__st."""
    node = shutil.which('node')
    if not node: return False
    url = 'file://' + os.path.abspath(page) + ('?' + query if query else '')
    r = subprocess.run([node, '-e', PW_JS, url, str(wait)], capture_output=True, text=True, env=node_env(), timeout=120)
    if r.returncode == 0: print(r.stdout.strip()); return True
    if 'Cannot find module' not in r.stderr: print('playwright check failed:', r.stderr.strip()[-400:])
    return False

PW_SHOTS = r"""
const { chromium } = require('playwright');
(async () => {
  const jobs = JSON.parse(require('fs').readFileSync(process.argv[1], 'utf8'));
  const b = await chromium.launch({ args: ['--no-sandbox'] });
  for (const j of jobs){
    const ctx = await b.newContext({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: j.scale });
    const pg = await ctx.newPage(); await pg.goto(j.url); await pg.waitForTimeout(j.wait);
    await pg.screenshot({ path: j.out }); await ctx.close();
  }
  await b.close();
})().catch(e => { console.error(e.message); process.exit(2); });
"""

def node_env():
    env = dict(os.environ)
    for d in ['/opt/node-tools/node_modules', os.path.expanduser('~/.npm-global/lib/node_modules')]:
        if os.path.isdir(d): env['NODE_PATH'] = d + os.pathsep + env.get('NODE_PATH', '')
    return env

def shots(page, jobs):
    """jobs: [(query, out, (w, h), scale, wait_ms)]. One Playwright browser for all of them when Playwright is
    installed (real-time waits: Chrome's CLI with --virtual-time-budget can hang while a figure animates);
    otherwise one Chrome CLI run per shot."""
    base = 'file://' + os.path.abspath(page)
    node = shutil.which('node')
    if node:
        spec = [{ 'url': base + ('?' + q if q else ''), 'out': os.path.abspath(o), 'w': sz[0], 'h': sz[1], 'scale': sc, 'wait': w }
                for q, o, sz, sc, w in jobs]
        fd, path = tempfile.mkstemp(suffix='.json'); os.write(fd, json.dumps(spec).encode()); os.close(fd)
        r = subprocess.run([node, '-e', PW_SHOTS, path], capture_output=True, text=True, env=node_env(), timeout=60 + 15*len(jobs))
        os.remove(path)
        if r.returncode == 0: return
        if 'Cannot find module' not in r.stderr: sys.exit('playwright shots failed: ' + r.stderr.strip()[-400:])
    for q, o, sz, sc, w in jobs: run(page, q, o, size=sz, scale=sc, budget=w)

def slug(q): return re.sub(r'[^A-Za-z0-9]+', '_', q).strip('_') or 'default'

def main():
    if len(sys.argv) < 3: sys.exit(__doc__)
    mode, page = sys.argv[1], sys.argv[2]
    outd = sys.argv[3] if len(sys.argv) > 3 and mode != 'errors' else None
    if outd: os.makedirs(outd, exist_ok=True)
    extra = sys.argv[4] if len(sys.argv) > 4 else ''
    j = lambda *a: '&'.join(x for x in a if x)
    if mode == 'verify':
        views = ['yaw=45', 'yaw=110', 'yaw=170', 'yaw=230', 'yaw=300', 'yaw=20&pitch=62', 'yaw=200&pitch=70']
        jobs = [(j('free=1', v, xr, extra), os.path.join(outd, f'v-{slug(v + xr)}.png'), (900, 800), 2, 2500)
                for v in views for xr in ['', 'xr=1&labels=1']]
        jobs.append((j('xr=1&labels=1', extra), os.path.join(outd, 'phone.png'), (390, 844), 2, 2500))
        shots(page, jobs)
        print('wrote', len(views)*2 + 1, 'shots to', outd)
    elif mode == 'press':
        seq = sys.argv[4]; budgets = sys.argv[5:] or ['1500', '3500', '6000']
        shots(page, [(j('free=1', 'press=' + seq, v), os.path.join(outd, f'p-{b}-{slug(v)}.png'), (900, 800), 2, int(b))
                     for b in budgets for v in ['', 'yaw=225', 'xr=1&labels=1']])
        print('wrote press shots to', outd)
    elif mode == 'errors':
        seq = sys.argv[3] if len(sys.argv) > 3 else ''
        q = j('free=1', 'press=' + seq if seq else '', sys.argv[4] if len(sys.argv) > 4 else '')
        if playwright_check(page, q): return
        # fallback: --dump-dom (fine for a page at rest; it can hang while a figure animates)
        dom = run(page, q, size=(700, 600), scale=1, budget=4000, dump=True)
        m = re.search(r'data-errors="([^"]*)"', dom)
        art = re.sub(r'data:[^"\')\s]+', '', dom)   # baked noise images are base64 and can spell NaN by chance
        print('errors:', m.group(1) if m else 'none'); print('NaN in drawing:', bool(re.search(r'\bNaN\b', art)))
    elif mode == 'social':
        # CSS widths stay above 560 px, where the page switches to its phone layout (numbered label badges)
        shots(page, [(j('clean=1', extra), os.path.join(outd, f'{name}.png'), size, sc, 3000)
                     for name, size, sc in [('feed-1080x1350', (600, 750), 1.8), ('square-1080', (600, 600), 1.8), ('wide-1920x1080', (960, 540), 2)]])
        print('wrote social stills to', outd)
    elif mode == 'spin':
        fr = tempfile.mkdtemp(prefix='fpspin-'); n = 48
        shots(page, [(j('free=1&clean=1', f'yaw={45 + 360*i/n:.1f}', extra), os.path.join(fr, f'f{i:03d}.png'), (720, 720), 1, 1200) for i in range(n)])
        if not shutil.which('ffmpeg'): sys.exit(f'frames in {fr}; install ffmpeg to join them')
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '16', '-i', os.path.join(fr, 'f%03d.png'),
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', os.path.join(outd, 'spin.mp4')], check=True)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', '16', '-i', os.path.join(fr, 'f%03d.png'),
                        '-vf', 'scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse', os.path.join(outd, 'spin.gif')], check=True)
        shutil.rmtree(fr, ignore_errors=True); print('wrote spin.mp4 and spin.gif to', outd)
    else: sys.exit(__doc__)

if __name__ == '__main__': main()

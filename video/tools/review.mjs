import fs from 'node:fs/promises';
import path from 'node:path';
import {existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {bundle} from '@remotion/bundler';
import {openBrowser, selectComposition, renderStill, renderMedia} from '@remotion/renderer';
import {prepareAssets, videoRoot} from './prepare-assets.mjs';

const onlyStills = process.argv.includes('--stills');
const browserExecutable = process.env.REMOTION_BROWSER_EXECUTABLE ||
  (existsSync('/usr/bin/chromium') ? '/usr/bin/chromium' : undefined);
if (!browserExecutable) throw new Error('Set REMOTION_BROWSER_EXECUTABLE to an installed Chrome/Chromium executable.');
await prepareAssets();
const reviewDir = path.join(videoRoot, 'review');
await fs.mkdir(reviewDir, {recursive: true});
const serveUrl = await bundle({entryPoint: path.join(videoRoot, 'src/index.ts'),
  publicDir: path.join(videoRoot, 'public'), outDir: path.join(videoRoot, '.cache/bundle')});
const browser = await openBrowser('chrome', {browserExecutable});
try {
  const common = {serveUrl, puppeteerInstance: browser, browserExecutable};
  const composition = await selectComposition({...common, id: 'WithinReach'});
  // Cover initial state, transfer, camera reveal and settled hold.
  const frames = [0, 66, 108, 156, 210, 269];
  for (const frame of frames) {
    await renderStill({...common, composition, frame, imageFormat: 'png',
      output: path.join(reviewDir, `frame-${String(frame).padStart(3, '0')}.png`)});
  }
  console.log(`Rendered ${frames.length} reference stills.`);
  if (!onlyStills) {
    let last = -1;
    await renderMedia({...common, composition, codec: 'h264', pixelFormat: 'yuv420p', muted: true, enforceAudioTrack: false,
      crf: 18, concurrency: 2, outputLocation: path.join(reviewDir, 'within-reach-motion-study.mp4'),
      onProgress: ({progress}) => {const step = Math.floor(progress * 4);
        if (step !== last) {console.log(`Video ${Math.round(progress * 100)}%`); last = step;}}
    });
    const inputPaths = ['src/index.ts', 'src/Root.tsx', 'src/WithinReach.tsx',
      'tools/prepare-assets.mjs', 'tools/review.mjs', 'package-lock.json', 'asset-manifest.json',
      'public/fonts/LiberationSans-Bold.ttf', '../design/within-reach/style-tokens.json'];
    const inputs = {};
    for (const name of inputPaths) inputs[name] = createHash('sha256')
      .update(await fs.readFile(path.resolve(videoRoot, name))).digest('hex');
    const artifacts = {};
    for (const name of [...frames.map((f) => `frame-${String(f).padStart(3, '0')}.png`), 'within-reach-motion-study.mp4']) {
      artifacts[name] = createHash('sha256').update(await fs.readFile(path.join(reviewDir, name))).digest('hex');
    }
    await fs.writeFile(path.join(reviewDir, 'render-manifest.json'), JSON.stringify({
      composition: composition.id, width: composition.width, height: composition.height,
      fps: composition.fps, frames: composition.durationInFrames,
      node: process.version, browser: execFileSync(browserExecutable, ['--version'], {encoding: 'utf8'}).trim(),
      inputs, artifacts,
    }, null, 2) + '\n');
    console.log('Rendered silent MP4. Run npm run verify for metadata and decode checks.');
  }
} finally {
  await browser.close({silent: true});
}

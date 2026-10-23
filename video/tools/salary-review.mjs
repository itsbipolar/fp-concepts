import fs from 'node:fs/promises';
import path from 'node:path';
import {existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {bundle} from '@remotion/bundler';
import {openBrowser, selectComposition, renderStill, renderMedia} from '@remotion/renderer';
import {prepareAssets, videoRoot} from './prepare-assets.mjs';
const onlyStills = process.argv.includes('--stills');
const browserExecutable = process.env.REMOTION_BROWSER_EXECUTABLE || (existsSync('/usr/bin/chromium') ? '/usr/bin/chromium' : undefined);
if (!browserExecutable) throw new Error('Set REMOTION_BROWSER_EXECUTABLE.');
await prepareAssets();
await fs.copyFile(path.join(videoRoot, 'projects/salary-dividend/audio/passage.wav'), path.join(videoRoot, 'public/assets/salary-dividend-passage.wav'));
const reviewDir = path.join(videoRoot, 'projects/salary-dividend/review');
await fs.mkdir(reviewDir, {recursive: true});
const serveUrl = await bundle({entryPoint: path.join(videoRoot, 'src/index.ts'), publicDir: path.join(videoRoot, 'public'), outDir: path.join(videoRoot, '.cache/salary-bundle')});
const browser = await openBrowser('chrome', {browserExecutable});
try {
  const common = {serveUrl, puppeteerInstance: browser, browserExecutable};
  const composition = await selectComposition({...common, id: 'SalaryDividendPassage'});
  const frames = [57, 78, 125, 156, 204, 249, 300, 359, 419];
  for (const frame of frames) await renderStill({...common, composition, frame, imageFormat: 'png', output: path.join(reviewDir, `frame-${String(frame).padStart(3, '0')}.png`)});
  execFileSync('ffmpeg', ['-v', 'error', '-y', '-pattern_type', 'glob', '-i', path.join(reviewDir, 'frame-*.png'), '-vf', 'scale=480:270,tile=3x3:padding=12:margin=12:color=0xfff9d8', '-frames:v', '1', path.join(reviewDir, 'contact-sheet.png')]);
  for (const [frame, name] of [[57, 'phone-opening.png'], [419, 'phone-hold.png']]) execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', path.join(reviewDir, `frame-${String(frame).padStart(3, '0')}.png`), '-vf', 'scale=390:-1', '-frames:v', '1', path.join(reviewDir, name)]);
  console.log('Rendered nine passage stills, contact sheet and phone previews.');
  if (!onlyStills) {
    let last = -1;
    await renderMedia({...common, composition, codec: 'h264', pixelFormat: 'yuv420p', audioCodec: 'aac', crf: 18, concurrency: 2, outputLocation: path.join(reviewDir, 'salary-dividend-passage.mp4'), onProgress: ({progress}) => {const step = Math.floor(progress * 4); if (step !== last) {console.log(`Video ${Math.round(progress * 100)}%`); last = step;}}});
    // AAC from the Remotion intermediate can extend past the visual endpoint.
    // Mux an exact 14-second review file, copying the rendered video unchanged.
    const movie = path.join(reviewDir, 'salary-dividend-passage.mp4');
    const trimmed = path.join(reviewDir, '.passage-trimmed.mp4');
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', movie, '-t', '14', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', trimmed]);
    await fs.rename(trimmed, movie);
    execFileSync('ffmpeg', ['-v', 'error', '-y', '-i', movie, '-vf', 'select=eq(n\\,57)+eq(n\\,78)+eq(n\\,84)+eq(n\\,141)+eq(n\\,156)+eq(n\\,204)+eq(n\\,249)+eq(n\\,320)+eq(n\\,419),scale=480:270,tile=3x3:padding=12:margin=12:color=0xfff9d8', '-frames:v', '1', path.join(reviewDir, 'decoded-contact-sheet.png')]);
    const inputPaths = ['src/index.ts', 'src/Root.tsx', 'src/salary-dividend/SalaryDividendPassage.tsx', 'tools/prepare-assets.mjs', 'tools/salary-review.mjs', 'tools/verify-salary.py', 'package-lock.json', 'asset-manifest.json', 'public/fonts/LiberationSans-Bold.ttf', 'projects/salary-dividend/audio/passage.wav', 'public/assets/salary-dividend-passage.wav'];
    const inputs = {}, artifacts = {};
    for (const name of inputPaths) inputs[name] = createHash('sha256').update(await fs.readFile(path.join(videoRoot, name))).digest('hex');
    for (const name of [...frames.map(f => `frame-${String(f).padStart(3, '0')}.png`), 'contact-sheet.png', 'phone-opening.png', 'phone-hold.png', 'decoded-contact-sheet.png', 'salary-dividend-passage.mp4']) artifacts[name] = createHash('sha256').update(await fs.readFile(path.join(reviewDir, name))).digest('hex');
    await fs.writeFile(path.join(reviewDir, 'render-manifest.json'), JSON.stringify({composition: composition.id, width: composition.width, height: composition.height, fps: composition.fps, frames: composition.durationInFrames, node: process.version, browser: execFileSync(browserExecutable, ['--version'], {encoding: 'utf8'}).trim(), inputs, artifacts}, null, 2) + '\n');
    console.log('Rendered passage MP4 with audio.');
  }
} finally {await browser.close({silent: true});}

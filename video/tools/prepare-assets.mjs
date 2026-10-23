import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';

export const videoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const repoRoot = path.dirname(videoRoot);
export async function prepareAssets() {
  const manifest = JSON.parse(await fs.readFile(path.join(videoRoot, 'asset-manifest.json'), 'utf8'));
  const destination = path.join(videoRoot, 'public/assets');
  await fs.mkdir(destination, {recursive: true});
  for (const asset of manifest.assets) {
    const source = path.resolve(repoRoot, asset.source);
    if (!source.startsWith(repoRoot + path.sep) || path.basename(asset.file) !== asset.file) {
      throw new Error(`Asset path outside expected roots: ${asset.id}`);
    }
    const bytes = await fs.readFile(source);
    if (createHash('sha256').update(bytes).digest('hex') !== asset.sha256) {
      throw new Error(`Source art changed: ${asset.source}`);
    }
    await fs.writeFile(path.join(destination, asset.file), bytes);
  }
  console.log(`Prepared ${manifest.assets.length} unchanged source assets.`);
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) await prepareAssets();

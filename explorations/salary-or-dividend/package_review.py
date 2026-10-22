"""Embed the lesson once per unique image and package a server-free review."""
from base64 import b64encode
from pathlib import Path
import json
import re
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent
page = (ROOT / 'index.html').read_text()
page = page.replace('<link rel="stylesheet" href="style.css">',
                    '<style>\n' + (ROOT / 'style.css').read_text() + '\n</style>')
for filename in ('model.js', 'app.js'):
    page = re.sub(r'(?m)^[ \t]*<script src="' + re.escape(filename)
                  + r'" defer></script>[ \t]*\n', '', page)

images = {}
paths = {}


def embed(match):
    path = (ROOT / match.group(1)).resolve()
    if path.suffix != '.png' or not path.is_file():
        raise ValueError(f'Unexpected asset: {path}')
    if path not in paths:
        key = f'art{len(paths)}'
        paths[path] = key
        images[key] = 'data:image/png;base64,' + b64encode(path.read_bytes()).decode()
    return f'data-embedded-src="{paths[path]}"'


page = re.sub(r'src="([^"]+)"', embed, page)
boot = '\n<script>\nconst embeddedArt=' + json.dumps(images, separators=(',', ':')) + ';\n'
boot += "document.querySelectorAll('[data-embedded-src]').forEach(el=>{el.src=embeddedArt[el.dataset.embeddedSrc];});\n"
boot += '\n'.join((ROOT / name).read_text().replace('</script', '<\\/script')
                  for name in ('model.js', 'app.js'))
boot += '\n</script>\n'
page = page.replace('</body>', boot + '</body>')
(ROOT / 'play.html').write_text(page)
with ZipFile(ROOT / 'salary-or-dividend.zip', 'w', ZIP_DEFLATED) as archive:
    archive.write(ROOT / 'play.html', 'Salary or dividend.html')
    archive.writestr('READ ME.txt',
        'Extract this ZIP, then open Salary or dividend.html in a modern browser.\n'
        'Choose Pay a salary or Pay a dividend. You can pause, replay, switch or reset.\n'
        'Tap the illustrated labels for more explanation. Artwork is embedded; no server or internet required.\n'
        'This is a qualitative visual prototype. It does not calculate tax, net cash or pension amounts.\n')
print(f'Packaged {len(images)} unique images into play.html and salary-or-dividend.zip.')

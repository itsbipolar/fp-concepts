"""Make the ownership interaction portable without a server."""
from base64 import b64encode
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parent
page = (root / 'index.html').read_text()
for path in sorted((root / 'assets').glob('*.png')):
    page = page.replace('assets/' + path.name, 'data:image/png;base64,' + b64encode(path.read_bytes()).decode())
(root / 'play.html').write_text(page)
with ZipFile(root / 'within-reach.zip', 'w', ZIP_DEFLATED) as archive:
    archive.write(root / 'play.html', 'Within reach.html')
    archive.writestr('READ ME.txt', 'Extract the ZIP, then open Within reach.html in a modern browser. Drag the company or owner, or use the buttons. The artwork is embedded and works without a server or internet.\n')
print('Packaged standalone play.html and within-reach.zip.')

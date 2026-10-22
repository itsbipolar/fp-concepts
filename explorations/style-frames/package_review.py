"""Package the review page with its PNG images embedded for offline viewing."""
from base64 import b64encode
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parent
page = (root / 'index.html').read_text()
for path in sorted((root / 'assets').glob('*.png')):
    page = page.replace('assets/' + path.name, 'data:image/png;base64,' + b64encode(path.read_bytes()).decode())
(root / 'review.html').write_text(page)
with ZipFile(root / 'style-frames.zip', 'w', ZIP_DEFLATED) as archive:
    archive.write(root / 'review.html', 'FP Concepts - Style Frames.html')
    archive.writestr('READ ME.txt', 'Extract the ZIP, then open FP Concepts - Style Frames.html in a modern browser. The images are embedded: no server or internet connection is needed.\n')
print('Packaged offline HTML and ZIP.')

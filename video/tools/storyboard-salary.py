"""Render the editable illustrated storyboard (requires Python Playwright + Chromium)."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "video/projects/salary-dividend"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path="/usr/bin/chromium", headless=True,
                                        args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 1280, "height": 1000}, device_scale_factor=1)
            page.goto(f"http://127.0.0.1:{server.server_port}/video/projects/salary-dividend/storyboard.html")
            page.wait_for_function("document.querySelectorAll('.panel').length === 7 && document.images.length > 0 && [...document.images].every(i => i.complete && i.naturalWidth > 0)")
            page.evaluate("document.fonts.ready")
            page.screenshot(path=str(PROJECT / "storyboard.png"), full_page=True)
            page.pdf(path=str(PROJECT / "storyboard.pdf"), format="A3", landscape=True,
                     print_background=True, prefer_css_page_size=True)
            print("Rendered seven illustrated storyboard frames, PNG and PDF.")
            browser.close()
    finally:
        server.shutdown()


if __name__ == "__main__":
    main()

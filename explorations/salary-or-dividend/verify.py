"""Exercise source and offline lesson with Chromium/Playwright.

Run package_review.py first. Requires Python Playwright and Chromium.
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from zipfile import ZipFile
import json
import shutil

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(REPO)))
Thread(target=server.serve_forever, daemon=True).start()
url = f'http://127.0.0.1:{server.server_port}/explorations/salary-or-dividend/'
checks = []
errors = []


def state(page):
    return page.evaluate('window.salaryLessonState')


def settled(page, choice):
    page.wait_for_function('(choice)=>window.salaryLessonState.choice===choice && window.salaryLessonState.beat===3 && !window.salaryLessonState.playing', arg=choice)
    page.wait_for_timeout(750)  # allow paper fold/ink motion to settle


def image_check(page):
    page.wait_for_function('Array.from(document.images).every(i=>i.complete && i.naturalWidth>0)')


try:
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=shutil.which('chromium'), args=['--no-sandbox'])
        context = browser.new_context(viewport={'width': 1440, 'height': 1000})
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(url)
        image_check(page)
        assert state(page)['choice'] is None and state(page)['beat'] == 0
        assert page.locator('#replay').is_disabled()
        assert page.locator('.record-line').count() == 2
        checks.append('Initial scene, images and preserved history')

        page.locator('#salary').focus()
        page.keyboard.press('Enter')
        page.wait_for_timeout(180)
        page.locator('#pause').click()
        before = state(page)
        page.wait_for_timeout(1250)
        assert state(page) == before and not before['playing']
        page.locator('#pause').click()
        settled(page, 'salary')
        assert page.locator('#salary').get_attribute('aria-pressed') == 'true'
        assert page.locator('.new-room-flap').evaluate('(el)=>getComputedStyle(el).opacity') == '1'
        assert page.locator('.record-line').count() == 2
        page.screenshot(path=str(ROOT / 'preview.png'), full_page=True)
        checks.append('Keyboard choice, pause/resume, salary stamp and unfolded room')

        page.locator('#cpp-record').focus()
        page.keyboard.press('Enter')
        assert page.locator('#detail-note').is_visible()
        assert 'pension' in page.locator('#detail-body').inner_text().lower()
        page.keyboard.press('Escape')
        assert page.locator('#detail-note').is_hidden()
        assert page.evaluate('document.activeElement.id') == 'cpp-record'
        checks.append('Accessible explanation and focus return')

        page.locator('#dividend').click()
        settled(page, 'dividend')
        assert page.locator('.new-room-flap').evaluate('(el)=>getComputedStyle(el).opacity') == '0'
        assert page.locator('.record-line').count() == 2
        assert page.locator('#rrsp-label').is_visible()
        assert 'No new room' in page.locator('#rrsp-label').inner_text()
        page.screenshot(path=str(ROOT / 'dividend-preview.png'), full_page=True)
        checks.append('Dividend leaves earlier CPP history and RRSP room intact')

        for choice in ('salary', 'dividend', 'salary', 'dividend'):
            page.locator('#' + choice).click()
            page.wait_for_timeout(90)
        settled(page, 'dividend')
        assert page.locator('.record-line').count() == 2
        page.locator('#replay').click()
        settled(page, 'dividend')
        checks.append('Rapid choice switching and replay do not accumulate effects')

        page.locator('#salary').click()
        page.wait_for_timeout(250)
        page.locator('#reset').click()
        page.wait_for_timeout(2300)
        assert state(page)['choice'] is None and state(page)['beat'] == 0
        assert page.locator('.new-room-flap').evaluate('(el)=>getComputedStyle(el).opacity') == '0'
        checks.append('Reset interrupts all pending sequence changes')

        page.locator('#salary').click()
        page.locator('#pause').click()
        page.emulate_media(reduced_motion='reduce')
        settled(page, 'salary')
        page.locator('#dividend').click()
        assert state(page)['beat'] == 3 and not state(page)['playing']
        checks.append('Reduced motion including preference change while paused')

        for width in (390, 320):
            page.set_viewport_size({'width': width, 'height': 844})
            page.locator('#salary').click()
            settled(page, 'salary')
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            assert page.locator('#cpp-record').is_visible()
            assert page.locator('#rrsp-room').is_visible()
            if width == 390:
                page.screenshot(path=str(ROOT / 'mobile-preview.png'), full_page=True)
        checks.append('390px and 320px layout; no horizontal overflow')

        # Managed Chromium blocks file: navigation. Serve the identical standalone
        # document, prove it loads no dependencies, then disconnect the network.
        offline = browser.new_context(reduced_motion='reduce', viewport={'width': 1100, 'height': 900})
        local = offline.new_page()
        requests = []
        local.on('request', lambda request: requests.append(request.url))
        local.on('pageerror', lambda error: errors.append(str(error)))
        standalone_url = url + 'play.html'
        local.goto(standalone_url)
        image_check(local)
        offline.set_offline(True)
        local.locator('#salary').click()
        assert state(local)['beat'] == 3
        local.locator('#dividend').click()
        assert state(local)['choice'] == 'dividend'
        assert requests == [standalone_url], requests
        checks.append('Standalone HTML makes one document request; interaction works after disconnect')
        browser.close()

    with ZipFile(ROOT / 'salary-or-dividend.zip') as archive:
        assert archive.testzip() is None
        assert archive.read('Salary or dividend.html') == (ROOT / 'play.html').read_bytes()
    checks.append('ZIP integrity and exact standalone content')
    assert not errors, errors
    print(json.dumps({'passed': checks, 'javascript_errors': errors,
                      'limitation': 'Managed browser blocks file: navigation; identical standalone HTML tested via local HTTP, then network disconnected.'}, indent=2))
finally:
    server.shutdown()
    server.server_close()

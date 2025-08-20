import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    page.goto("https://prom.ua/ua/")
    yield page
    # context.close()
    # browser.close()
    page.pause()  
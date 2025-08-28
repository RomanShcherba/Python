import pytest
from playwright.async_api import async_playwright
import pytest_asyncio

@pytest_asyncio.fixture
async def page():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()
        await page.goto("https://prom.ua/ua/")
        yield page
        # await context.close()
        # await browser.close()
        await page.pause()

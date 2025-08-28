from functools import wraps
import logging
from playwright.sync_api import Page



logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
logger = logging.getLogger(__name__)

def log_action(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logger.info(f"[{self.__class__.__name__}]Finished executing {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @log_action
    async def navigate(self, url: str):
        await self.page.goto(url)

    @log_action
    async def click(self, locator: str):
        await self.page.click(locator)

    @log_action
    async def send_keys(self, locator: str, text: str, press_enter=False):
        await self.page.fill(locator, text)
        if press_enter:
            await self.page.press(locator, "Enter")

    @log_action
    async def get_text(self, locator: str):
        return await self.page.inner_text(locator)

    @log_action
    async def get_title(self):
        return await self.page.title()

    @log_action
    async def scroll_into_view(self, locator: str):
        element = self.page.locator(locator)
        await element.scroll_into_view_if_needed()
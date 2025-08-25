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
    def navigate(self, url: str):
        self.page.goto(url)

    @log_action
    def click(self, locator: str):
        self.page.click(locator)

    @log_action
    def send_keys(self, locator: str, text: str, press_enter=False):
        self.page.fill(locator, text)
        if press_enter:
            self.page.press(locator, "Enter")

    @log_action
    def get_text(self, locator: str):
        return self.page.inner_text(locator)

    @log_action
    def get_title(self):
        return self.page.title()

    @log_action
    def scroll_into_view(self, locator: str):
        element = self.page.locator(locator)
        element.scroll_into_view_if_needed()
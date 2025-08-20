from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.click(locator)

    def send_keys(self, locator: str, text: str, press_enter=False):
        self.page.fill(locator, text)
        if press_enter:
            self.page.press(locator, "Enter")

    def get_text(self, locator: str):
        return self.page.inner_text(locator)

    def get_title(self):
        return self.page.title()

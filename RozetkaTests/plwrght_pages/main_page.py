from socket import timeout
from plwrght_pages.base_page import BasePage, log_action
from utils.test_data import TestData

class MainPage(BasePage):
    search_input = "xpath=//input[@type='search']"
    search_button = "xpath=//button[@type='submit']"
    cabinet_sidebar_button = "//button[@title='Кабінет']"
    sign_in_button = "xpath=//button[@data-qaid='sign_in_mob_sidebar']"
    login_enter_confirmation = "xpath=//span[text()='Вхід']"
    login_button = "xpath=//div[@data-qaid='email_btn']"
    sidebar_electronic_button = "xpath=//span[contains(text(),'Техніка та електроніка')]"
    notification_button = "xpath=//button[@data-qaid='notification_btn']"
    notification_message = "xpath=//span[(text())='Всі звісточки під рукою']"
    email_input = "xpath=//input[@id='email_field']"

    def __init__(self, page):
        super().__init__(page)


    @log_action
    async def enter_search_text(self, search_text):
        await self.send_keys(self.search_input, search_text)

    @log_action
    async def click_search_button(self):
        await self.click(self.search_button)

    @log_action
    async def click_cabinet_sidebar_button(self):
        await self.click(self.cabinet_sidebar_button)

    @log_action
    async def click_sign_in_button(self):
        await self.click(self.sign_in_button)

    @log_action
    async def is_login_enter_message_displayed(self, timeout: int = 5000):
        await self.page.wait_for_selector(self.login_enter_confirmation, timeout=timeout)
        return await self.page.is_visible(self.login_enter_confirmation)
    
    @log_action
    async def click_login_button(self):
        await self.click(self.login_button)
          
    @log_action
    async def click_sidebar_electronic_button(self, timeout: int = 5000):
        await self.page.wait_for_selector(self.sidebar_electronic_button, timeout=timeout)
        await self.click(self.sidebar_electronic_button)

    @log_action
    async def click_notification_button(self):
        await self.click(self.notification_button)

    @log_action
    async def is_notification_message_displayed(self, timeout: int = 5000):
        await self.page.wait_for_selector(self.notification_message, timeout=timeout)
        return await self.page.is_visible(self.notification_message)
    
    @log_action
    async def enter_email(self, email: str):
        await self.send_keys(self.email_input, email)

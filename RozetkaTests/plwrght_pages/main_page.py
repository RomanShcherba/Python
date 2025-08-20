from plwrght_pages.base_page import BasePage

class MainPage(BasePage):
    search_input = "xpath=//input[@type='search']"
    search_button = "xpath=//button[@type='submit']"
    cabinet_sidebar_button = "//button[@title='Кабінет']"
    sign_in_button = "xpath=//button[@data-qaid='sign_in_mob_sidebar']"
    login_enter_confirmation = "xpath=//span[text()='Вхід']"
    phone_input = "xpath=//input[@id='phone_field']"


    def __init__(self, page):
        super().__init__(page)

    def enter_search_text(self, search_text):
        self.send_keys(self.search_input, search_text)
    
    def click_search_button(self):
        self.click(self.search_button)

    def click_cabinet_sidebar_button(self):
        self.click(self.cabinet_sidebar_button)

    def click_sign_in_button(self):
        self.click(self.sign_in_button)
 
    def is_login_enter_message_displayed(self, timeout: int = 5000):
        self.page.wait_for_selector(self.login_enter_confirmation, timeout=timeout)
        return self.page.is_visible(self.login_enter_confirmation)
    
    def enter_phone_number(self, phone_number):
        self.send_keys(self.phone_input, phone_number)
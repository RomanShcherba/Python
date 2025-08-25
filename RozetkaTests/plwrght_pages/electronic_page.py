from pages.base_page import log_action
from plwrght_pages.base_page import BasePage

class ElectronicPage(BasePage):

    confirmation_electronics_page_text = "xpath = //h1[contains(.,'Техніка та електроніка')]"
    filter_country_producer_button = "xpath = //button[@data-qatype='Країна виробник']"
    producer_checkbox = "xpath = //span[@class='_0cNvO mxBXr'][contains(text(),'Китай')]"

    @log_action
    def is_confirmation_electronics_page_displayed(self, timeout: int = 5000):
        self.page.wait_for_selector(self.confirmation_electronics_page_text, timeout=timeout)
        return self.page.is_visible(self.confirmation_electronics_page_text)
    
    @log_action
    def click_filter_producer_button(self):
        self.click(self.filter_country_producer_button)

    @log_action
    def click_producer_china_checkbox(self):
        self.scroll_into_view(self.producer_checkbox)
        self.click(self.producer_checkbox)

    

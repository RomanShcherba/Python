from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutPage(BasePage):
    checkout_message = (By.XPATH, "//h1[text()='Оформлення замовлення']")

    def __init__(self, driver):
        self.driver = driver

    def get_checkout_message(self):
        self.wait_for_visible(self.checkout_message)
        return self.get_text(self.checkout_message)
    

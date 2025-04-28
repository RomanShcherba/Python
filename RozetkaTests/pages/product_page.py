from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    add_to_cart_button = (By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium buy-button--tile']")
    pop_up_cart = (By.XPATH, "//span[@class='cart-product__title']")
    option_button = (By.XPATH, "//button[@id='cartProductActions0']")
    delete_button = (By.XPATH, "//button[@class='button button--medium button--with-icon button--link']")
    get_empty_cart_message = (By.XPATH, "//h4[text()='Кошик порожній']")

    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_to_cart_button(self):
        self.click(self.add_to_cart_button)

    def get_pop_up_cart(self):
        return self.get_text(self.pop_up_cart)
    
    def click_option_button(self):
        self.click(self.option_button)

    def click_delete_button(self):
        self.click(self.delete_button)
    
    def get_message_cart(self):
        return self.get_text(self.get_empty_cart_message)
       
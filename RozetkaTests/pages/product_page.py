from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    click_buy_button = (By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium buy-button--tile']")
    click_open_cart = (By.XPATH, "//div[@class = 'layout'] //button[@class='header-cart__button']")
    pop_up_cart = (By.XPATH, "//span[@class='cart-product__title']")
    option_button = (By.XPATH, "//button[@id='cartProductActions0']")
    delete_button = (By.XPATH, "//button[@class='button button--medium button--with-icon button--link']")
    get_empty_cart_message = (By.XPATH, "//h4[text()='Кошик порожній']")
    
    def __init__(self, driver):
        self.driver = driver

    def buy_button(self):
        self.wait_for_visible(self.click_buy_button).click()
        

    def open_cart_button(self):
        self.wait_for_visible(self.click_open_cart).click()

    def get_pop_up_cart(self):
        self.wait_for_visible(self.pop_up_cart)
        return self.get_text(self.pop_up_cart)
    
    def click_option_button(self):
        self.wait_for_clickable(self.option_button).click()

    def click_delete_button(self):
        self.wait_for_clickable(self.delete_button).click()
    
    def get_message_cart(self):
        self.wait_for_visible(self.get_empty_cart_message)
        return self.get_text(self.get_empty_cart_message)
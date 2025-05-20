from functools import wraps
from pages.base_page import BasePage, log_action
from selenium.webdriver.common.by import By
import logging



class ProductPage(BasePage):
    click_buy_button = (By.XPATH, "//button[@class='buy-button button button--with-icon button--green button--medium buy-button--tile']")
    click_open_cart = (By.XPATH, "//div[@class = 'layout'] //button[@class='header-cart__button']")
    pop_up_cart = (By.XPATH, "//span[@class='cart-product__title']")
    option_button = (By.XPATH, "//button[@id='cartProductActions0']")
    delete_button = (By.XPATH, "//button[@class='button button--medium button--with-icon button--link']")
    get_empty_cart_message = (By.XPATH, "//h4[text()='Кошик порожній']")
    checkout_button = (By.XPATH, "//a[@class ='button button--green button_size_large cart-receipt__submit']")

    def __init__(self, driver):
        self.driver = driver

    @log_action
    def buy_button(self):
        self.wait_for_visible(self.click_buy_button).click()
        
    @log_action
    def open_cart_button(self):
        self.wait_for_visible(self.click_open_cart).click()

    @log_action
    def get_pop_up_cart(self):
        self.wait_for_visible(self.pop_up_cart)
        return self.get_text(self.pop_up_cart)
    
    @log_action
    def click_option_button(self):
        self.wait_for_clickable(self.option_button).click()
        if self.wait_for_clickable(self.option_button):
            logging.info("Option button is visible")
        else:
            logging.info("Option button is not visible")

    @log_action
    def click_delete_button(self):
        self.wait_for_clickable(self.delete_button).click()
    
    @log_action
    def get_message_cart(self):
        self.wait_for_visible(self.get_empty_cart_message)
        return self.get_text(self.get_empty_cart_message)
    
    @log_action
    def click_checkout_button(self):
        self.wait_for_clickable(self.checkout_button).click()
       
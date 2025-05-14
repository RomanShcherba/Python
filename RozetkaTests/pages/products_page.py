from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class ProductsPage(BasePage):
    add_to_cart_button = (By.XPATH, "(//button[@class='buy-button goods-tile__buy-button'])[1]")
    pop_up_cart = (By.XPATH, "//span[@class='cart-product__title']")
    open_cart_button = (By.XPATH, "//div[@class = 'layout'] //button[@class='header-cart__button']")
    cart_products_number = (By.XPATH, "//span[@class='badge']")
    click_on_product = (By.XPATH, "//div[@data-goods-id='410219112']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_to_product(self):
        self.wait_for_clickable(self.click_on_product).click()

    def click_add_to_cart_button(self):
        button = self.wait_for_clickable(self.add_to_cart_button)
        
        button.click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "buy-button_state_in-cart"))
        )

    def click_open_cart_button(self):
        self.wait_for_clickable(self.open_cart_button).click()

    def get_pop_up_cart(self):
        self.wait_for_visible(self.pop_up_cart)
        return self.get_text(self.pop_up_cart)
    
    def confirm_added_to_cart(self):
        self.wait_for_visible(self.cart_products_number)
        return self.cart_products_number
       
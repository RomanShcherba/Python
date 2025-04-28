from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    
    bycicle_message = (By.XPATH, "//h1[text()='Велосипеди']")
    product_search_result = (By.XPATH, "//div[@class='goods-tile__inner'][1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_bycicle_message(self):
        return self.get_text(self.bycicle_message)
    
    def click_product_search_result(self):
        self.click(self.product_search_result)
    
    

    
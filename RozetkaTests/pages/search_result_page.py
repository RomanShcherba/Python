from pages.base_page import BasePage, log_action
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    
    bycicle_message = (By.XPATH, "//h1[text()='Велосипеди']")
    product_search_result = (By.XPATH, "//div[@data-goods-id='410219112']")
    multiple_results = (By.XPATH, "//h1[@class='catalog-heading']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @log_action
    def get_bycicle_message(self):
        self.wait_for_visible(self.bycicle_message)
        return self.get_text(self.bycicle_message)
    
    @log_action
    def click_product_search_result(self):
        self.wait_for_clickable(self.product_search_result).cklick()

    @log_action
    def get_results_message(self):
        self.wait_for_visible(self.multiple_results)
        return self.get_text(self.multiple_results)
    
    

    
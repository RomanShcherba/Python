
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryProductsPage(BasePage):

    category_notebooks = (By.XPATH, "//img[@alt='Ноутбуки']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_category_notebooks(self):
        self.wait_for_clickable(self.category_notebooks).click()

    def scroll_down(self):
        self.wait_for_visible(self.category_notebooks)
        self.scroll_into_view(self.category_notebooks)
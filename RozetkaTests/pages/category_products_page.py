from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryProductsPage(BasePage):

    category_notebooks = (By.XPATH, "//img[@alt='Ноутбуки']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_category_notebooks(self):
        self.click(self.category_notebooks)
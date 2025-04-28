from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    catalogue = (By.XPATH, "//button[contains(@class,'button button--medium')]")
    notebooks = (By.XPATH, "//a[text() = ' Ноутбуки та комп’ютери ']")
    search_input = (By.XPATH, "//input[@name='search']")
    search_button = (By.XPATH, "//button[text()=' Знайти ']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_catalogue(self):
        self.click(self.catalogue)

    def click_notebooks(self):
        self.click(self.notebooks)
    
    def enter_search_text(self, query):
        self.click(self.search_input)
        self.send_keys(self.search_input, query)

    def click_search_button(self):
        self.click(self.search_button)
        
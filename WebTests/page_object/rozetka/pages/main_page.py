from selenium.webdriver.common.by import By
from page_object.rozetka.pages.base_page import BasePage


class MainPage(BasePage):

    # Locators
    sidebar_notebooks = (By.XPATH, "//a[text() = ' Ноутбуки та комп’ютери ']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_notebooks(self):
        self.click(self.sidebar_notebooks)
        
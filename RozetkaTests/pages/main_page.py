from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    catalogue = (By.XPATH, "//button[contains(@class,'button button--medium')]")
    notebooks = (By.XPATH, "(//ul[@class='list']//a)[1]")
    search_input = (By.XPATH, "//input[@name='search']")
    search_button = (By.XPATH, "//button[text()=' Знайти ']")
    catalogue_list = (By.XPATH, "//ul[@class='list']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_catalogue(self):
        self.wait_for_clickable(self.catalogue).click()

    def click_notebooks(self):
        self.wait_for_clickable(self.notebooks).click()
    
    def enter_search_text(self, query):
        self.wait_for_clickable(self.search_input).click()
        self.send_keys(self.search_input, query)

    def click_search_button(self):
         self.wait_for_clickable(self.search_button).click()
    
    def get_catalogue_list(self):
        return self.get_text(self.catalogue_list)
        
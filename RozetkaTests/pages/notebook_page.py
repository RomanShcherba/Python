from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class NotebookPage(BasePage):
    sort_by_cheap = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='cheap']")
    sort_by_expensive = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='expensive']")
    sort_by_new = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='novelty']")
    sort_by_rank = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='rank']")
    dell_checkbox = (By.XPATH, "(//div[contains(@class,'scrollbar custom-child-scrollbar')]//a)[4]")
    dell_notebook_message = (By.XPATH, "//h1[contains(text(),'Ноутбуки Dell')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sort_expensive(self):
        self.wait_for_clickable(self.sort_by_expensive).click()

    def click_dell_checkbox(self):
        self.wait_for_clickable(self.dell_checkbox).click()

    def get_dell_notebooks_message(self):
        self.wait_for_visible(self.dell_notebook_message)
        return self.get_text(self.dell_notebook_message)

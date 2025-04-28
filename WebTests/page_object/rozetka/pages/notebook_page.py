from selenium.webdriver.common.by import By
from page_object.rozetka.pages.base_page import BasePage



class NotebookPage(BasePage):
    sort_by_cheap = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='cheap']")
    sort_by_expensive = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='expensive']")
    sort_by_new = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='novelty']")
    sort_by_rank = (By.XPATH, "//select[@class='select-css setting-sorting font-rozetka']//option[@value='rank']")
    asus_checkbox = (By.XPATH, "//rz-indexed-link[@data-id='ASUS']")
    asus_notebooks_list = (By.XPATH, "//h1[text()='Ноутбуки ASUS']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sort_expensive(self):
        self.click(self.sort_by_expensive)

    def click_asus_checkbox(self):
        self.click(self.asus_checkbox)

    def get_asus_notebooks_list(self):
        return self.get_text(self.asus_notebooks_list)

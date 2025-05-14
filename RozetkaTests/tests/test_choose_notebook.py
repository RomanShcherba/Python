from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.category_products_page import CategoryProductsPage
from pages.main_page import MainPage
from pages.notebook_page import NotebookPage
from tests.base_test import BaseTest


class ChooseNotebooks(BaseTest):
    def test_choose_notebook(self):
        main_page = MainPage(self.driver) 
        main_page.click_catalogue()
        main_page.click_notebooks()
        category_products_page = CategoryProductsPage(self.driver)
        category_products_page.click_category_notebooks()
        notebook_page = NotebookPage(self.driver)
        notebook_page.sort_expensive()
        notebook_page.click_dell_checkbox()
        actual_message = notebook_page.get_dell_notebooks_message()
        expected_message = "Ноутбуки Dell"
        assert actual_message == expected_message

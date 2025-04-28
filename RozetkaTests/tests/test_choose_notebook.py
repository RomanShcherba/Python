import time
from pages.category_products_page import CategoryProductsPage
from pages.main_page import MainPage
from pages.notebook_page import NotebookPage
from tests.base_test import BaseTest


class ChooseNotebooks(BaseTest):
    def test_choose_notebook(self):
        main_page = MainPage(self.driver)
        time.sleep(2)
        main_page.click_notebooks()
        time.sleep(2)
        category_products_page = CategoryProductsPage(self.driver)
        category_products_page.click_category_notebooks()
        notebook_page = NotebookPage(self.driver)
        notebook_page.sort_expensive()
        time.sleep(2)
        notebook_page.click_asus_checkbox()
        time.sleep(2)
        actual_message = notebook_page.get_asus_notebooks_message()
        expected_message = "Ноутбуки ASUS"
        time.sleep(2)
        assert actual_message == expected_message

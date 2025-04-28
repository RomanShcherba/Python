from page_object.rozetka.pages.category_products_page import CategoryProductsPage
from page_object.rozetka.pages.main_page import MainPage
from page_object.rozetka.pages.notebook_page import NotebookPage
from page_object.rozetka.tests.base_test import BaseTest


class ChooseNotebooks(BaseTest):
    def test_choose_notebook(self):
        main_page = MainPage(self.driver)
        main_page.click_notebooks()
        category_products_page = CategoryProductsPage(self.driver)
        category_products_page.click_category_notebooks()
        notebook_page = NotebookPage(self.driver)
        notebook_page.sort_expensive()
        notebook_page.click_asus_checkbox()
        asus_notebooks_list = notebook_page.get_asus_notebooks_list()
        assert(asus_notebooks_list)




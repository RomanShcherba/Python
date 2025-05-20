from selenium.webdriver.common.by import By
from pages.category_products_page import CategoryProductsPage
from pages.main_page import MainPage
from pages.notebook_page import NotebookPage


def test_choose_notebook(driver):
        main_page = MainPage(driver)
        main_page.click_catalogue()
        main_page.click_notebooks()
        category_products_page = CategoryProductsPage(driver)
        category_products_page.scroll_down()
        category_products_page.click_category_notebooks()
        notebook_page = NotebookPage(driver)
        notebook_page.sort_expensive()
        notebook_page.click_dell_checkbox()
        actual_message = notebook_page.get_dell_notebooks_message()
        expected_message = "Ноутбуки Dell"
        assert actual_message == expected_message

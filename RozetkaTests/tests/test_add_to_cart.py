from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage
from tests.base_test import BaseTest
from utils.test_data import TestData


class TestAddToCart(BaseTest):
    def test_search(self):
        main_page = MainPage(self.driver)
        main_page.enter_search_text(TestData.search_input)
        main_page.click_search_button()
        products_page = ProductsPage(self.driver)
        products_page.click_to_product()
        product_page = ProductPage(self.driver)
        product_page.buy_button()
        product_page.open_cart_button()
        product_page.get_pop_up_cart()
        actual_message = products_page.get_pop_up_cart()
        expected_message = TestData.product_name
        assert actual_message == expected_message
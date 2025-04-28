import time
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_result_page import SearchResultPage
from tests.base_test import BaseTest
from utils.test_data import TestData


class TestAddToCart(BaseTest):
    def test_search(self):
        main_page = MainPage(self.driver)
        time.sleep(3)
        main_page.enter_search_text(TestData.search_input)
        time.sleep(3)
        main_page.click_search_button()
        time.sleep(3)
        search_result_page = SearchResultPage(self.driver)
        search_result_page.click_product_search_result()
        time.sleep(3)
        product_page = ProductPage(self.driver)
        product_page.click_add_to_cart_button()
        time.sleep(3)
        product_page.get_pop_up_cart()
        actual_message = product_page.get_pop_up_cart()
        expected_message = TestData.product_name
        time.sleep(2)
        assert actual_message == expected_message


        
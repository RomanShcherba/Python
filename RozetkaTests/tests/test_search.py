import time
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from tests.base_test import BaseTest
from utils.test_data import TestData


class Search(BaseTest):
    def test_search(self):
        main_page = MainPage(self.driver)
        time.sleep(3)
        main_page.enter_search_text(TestData.query)
        time.sleep(3)
        main_page.click_search_button()
        time.sleep(3)
        search_result_page = SearchResultPage(self.driver)
        actual_message = search_result_page.get_bycicle_message()
        expected_message = "Велосипеди"
        assert actual_message == expected_message

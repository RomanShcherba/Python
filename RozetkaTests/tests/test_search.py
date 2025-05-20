from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from utils.test_data import TestData



def test_search(driver):
        main_page = MainPage(driver)
        main_page.enter_search_text(TestData.query)
        main_page.click_search_button()
        search_result_page = SearchResultPage(driver)
        actual_message = search_result_page.get_bycicle_message()
        expected_message = TestData.query
        assert actual_message == expected_message

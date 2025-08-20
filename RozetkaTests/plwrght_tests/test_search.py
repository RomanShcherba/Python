from plwrght_pages.search_result_page import SearchResultPage
from plwrght_pages.main_page import MainPage
from utils.test_data import TestData

def test_search(page):
    main_page = MainPage(page)
    main_page.enter_search_text(TestData.search_text)
    main_page.click_search_button()
    search_result_page = SearchResultPage(page)
    assert search_result_page.is_search_result_displayed()
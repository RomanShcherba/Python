import pytest
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage


test_data = [
    ("Ноутбук", "Ноутбуки"),
    ("Телефон", "Мобільні телефони"),
    ("Планшет", "Планшети"),
] 
@pytest.mark.parametrize("query, expected_message", test_data)

def test_search(driver, query, expected_message):
    main_page = MainPage(driver)
    main_page.enter_search_text(query)
    main_page.click_search_button()

    search_result_page = SearchResultPage(driver)
    search_result_page.get_results_message()
    actual_message = search_result_page.get_results_message()

    assert actual_message == expected_message


    
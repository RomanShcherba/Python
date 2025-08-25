from plwrght_pages.electronic_page import ElectronicPage
from plwrght_pages.main_page import MainPage

def test_search_by_filters(page):
    main_page = MainPage(page)
    main_page.click_sidebar_electronic_button()
    electronic_page = ElectronicPage(page)
    electronic_page.click_filter_producer_button()
    electronic_page.click_producer_china_checkbox()
    
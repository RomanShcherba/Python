from plwrght_pages.electronic_page import ElectronicPage
from plwrght_pages.main_page import MainPage

def test_search_by_sidebar(page):
    main_page = MainPage(page)
    main_page.click_sidebar_electronic_button()
    electronic_page = ElectronicPage(page)
    assert electronic_page.is_confirmation_electronics_page_displayed()
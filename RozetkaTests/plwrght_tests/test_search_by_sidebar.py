import pytest
from plwrght_pages.electronic_page import ElectronicPage
from plwrght_pages.main_page import MainPage

import pytest

@pytest.mark.asyncio
async def test_search_by_sidebar(page):
    main_page = MainPage(page) 
    await main_page.click_sidebar_electronic_button("//span[contains(text(),'Техніка та електроніка')]")

    electronic_page = ElectronicPage(page)
    assert await electronic_page.is_confirmation_electronics_page_displayed()
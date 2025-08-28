import pytest
from plwrght_pages.main_page import MainPage

@pytest.mark.asyncio
async def test_check_notifications(page):
    main_page = MainPage(page)
    await main_page.click_notification_button()
    assert await main_page.is_notification_message_displayed()
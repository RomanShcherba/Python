from plwrght_pages.main_page import MainPage
from utils.test_data import TestData

# def test_sign_in_possibility(page):
#     main_page = MainPage(page)
#     main_page.click_cabinet_sidebar_button()
#     main_page.click_sign_in_button()
#     assert main_page.is_login_enter_message_displayed(timeout=5000)
   
def test_enter_phone_number(page):
    main_page = MainPage(page)
    main_page.click_cabinet_sidebar_button()
    main_page.click_sign_in_button()
    main_page.enter_phone_number(TestData.phone_number)
    
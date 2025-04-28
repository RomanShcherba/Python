from pages.change_password_page import ChangePaswordPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utils.test_data import TestData

class TestChangePassword(BaseTest):
    def test_change_password(self):
        login_page = LoginPage(self.driver)
        change_password_page = ChangePaswordPage(self.driver)
        expected_message = "Password confirmation does not match password!"
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        my_account_page =  login_page.click_login_button()
        my_account_page.click_right_menu_page()
        change_password_page.change_password(
        "InvalidPassword", "InvalidConfirmPassword")
        actual_message = change_password_page.get_confirmation_error_message()
        assert actual_message == expected_message
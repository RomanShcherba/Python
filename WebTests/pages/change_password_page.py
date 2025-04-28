from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage
from utils.locators import ChangeLocatorsFields


class ChangePaswordPage(BasePage):

    def __init__(self, driver):
        self.locatte = ChangeLocatorsFields
        super().__init__(driver)

    def change_password(self, password, confirm_password):
        self.set(self.locatte.password_field, password)
        self.set(self.locatte.confirm_password_field, confirm_password)
        self.click(self.locatte.continue_button)
        return MyAccountPage(self.driver)
    
    def get_confirmation_error_message(self):
        return self.get_text(self.locatte.confirmation_error_message)

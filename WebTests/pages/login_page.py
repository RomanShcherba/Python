from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage


class LoginPage(BasePage):
    email_address_field = (By.XPATH, "//input[@name = 'email']")
    password_field = (By.XPATH, "//input[@name = 'password']")
    login_button = (By.XPATH, "//input[@value = 'Login']")
    warning_message = (By.XPATH, "//div[@class = 'alert alert-danger alert-dismissible']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_email_address(self, email):
        self.set(self.email_address_field, email)
        #self.driver.find_element(*self.email_address_field).send_keys(email)
    
    def set_password(self, password):
        self.set(self.password_field, password)
    
    def click_login_button(self):
        self.click(self.login_button)
        return MyAccountPage(self.driver)
    
    def log_into_app(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

    def invalid_creds(self, invemail, invpassword):
        self.set_email_address(invemail)
        self.set_password(invpassword)
        self.click_login_button()

    def get_warning_message(self):
        return self.get_text(self.warning_message)
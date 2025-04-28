from selenium.webdriver.common.by import By

class ChangeLocatorsFields:
    password_field = (By.XPATH, "//input[@name='password']")
    confirm_password_field = (By.XPATH,"//input[@name='confirm']")
    continue_button = (By.XPATH,"//input[@type='submit']")
    confirmation_error_message = (By.XPATH,"//div[@class='text-danger']")
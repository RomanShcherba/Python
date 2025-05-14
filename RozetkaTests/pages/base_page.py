from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        self.find(locator).click()
    
    def send_keys(self, locator, text):
        element = self.find(locator)
        element.send_keys(text)
    
    def get_text(self, locator):
        return self.find(locator).text
    
    def get_title(self):
        return self.driver.title
    
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
    )

    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_text(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

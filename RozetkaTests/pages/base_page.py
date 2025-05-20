from functools import wraps
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
logger = logging.getLogger(__name__)

def log_action(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logger.info(f"[{self.__class__.__name__}]Finished executing {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper
class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @log_action
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    @log_action
    def click(self, locator):
        self.find(locator).click()
    
    @log_action
    def send_keys(self, locator, text):
        element = self.find(locator)
        element.send_keys(text)
    
    @log_action
    def get_text(self, locator):
        return self.find(locator).text
    
    @log_action
    def get_title(self):
        return self.driver.title
    
    @log_action
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
    )

    @log_action
    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    @log_action
    def wait_for_text(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
    @log_action
    def scroll_into_view(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)    
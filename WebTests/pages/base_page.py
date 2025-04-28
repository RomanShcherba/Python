from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        self.find(locator).click()

    def set(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)
    
    def get_text(self, locator):
        return self.find(locator).text
    
    def get_title(self):
        return self.driver.title
    
    def click_right_menu_page(self):
        page = By.XPATH, "//aside[@id='column-right']//a[contains(text(), 'Password')]"
        self.click(page)

    # def page(self):
    #     return By.XPATH, "//aside[@id='column-right']//a[contains(text(), 'Password')]"

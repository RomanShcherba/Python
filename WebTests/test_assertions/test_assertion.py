
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# class AssertionsTest():
#     pass

def test_assert():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rozetka.com.ua/ua/")
    driver.find_element(By.XPATH, "(//a[contains(@class,'category-link px-3')])[1]").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)

    driver.find_element(By.XPATH, "//img[@alt='Ноутбуки']").click()
    assert driver.find_element(By.XPATH, "//h1[normalize-space(text())='Ноутбуки']").is_displayed(), "Element is not displayed"
    driver.quit()
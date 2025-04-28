from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    search_box = driver.find_element(By.XPATH,"//input[@data-autocomplete='5']")
    search_box.click()
    search_box.send_keys("iPhone")   
    driver.find_element(By.XPATH,"//button[contains(text(), 'Search')]").click()
    time.sleep(5)
    assert driver.find_element(By.XPATH, "//h4[contains(text(), 'iPhone')]").is_displayed(), "Element is not displayed"
    

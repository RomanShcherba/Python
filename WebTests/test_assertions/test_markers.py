import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By\

@pytest.mark.smoke
def test_ajax_form():
    driver = webdriver.Chrome() 
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
    title = driver.find_element(By.XPATH,"//input[@id= 'title']")
    title.click()
    title.send_keys("Hello World")
    textarea = driver.find_element(By.XPATH, "//textarea[@id='description']")
    textarea.click()
    textarea.send_keys("Hello World")
    driver.find_element(By.XPATH,"//input[@name= 'btn-submit']").click()
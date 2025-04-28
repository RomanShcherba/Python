from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_subset():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
  driver.find_element(By.XPATH,"//input[@id= 'user-message']").click()
  driver.find_element(By.XPATH,"//input[@id= 'user-message']").send_keys("Hello World")
  driver.find_element(By.XPATH,"//button[@id='showInput']").click()
  message = driver.find_element(By.XPATH,"//p[contains(text(), 'Hello World')]").text
  time.sleep(2)
  assert message == "Hello World"
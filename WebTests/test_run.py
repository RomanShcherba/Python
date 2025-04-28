from selenium import webdriver

def test_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rozetka.com.ua/ua/")
    driver.quit()


def test2_lambdatest():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rozetka.com.ua/ua/")
    driver.quit()

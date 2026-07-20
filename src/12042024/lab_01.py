from selenium import webdriver
import time


def test_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    time.sleep(5)
    print(driver.title)

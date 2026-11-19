from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_vwo_Login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.ID,"btn-make-appointment").click()
    driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID,"btn-login").click()
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    print(driver.current_url)

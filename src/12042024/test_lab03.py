import allure
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


allure.title("verify the invalid login")
allure.description("tc#1- login check with invalid credentials")
@pytest.mark.smoke
def test_sauceLogin():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("abs")
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("jj")
    list_of_a_tag = driver.find_elements(By.TAG_NAME,"input")
    login=list_of_a_tag[2]
    login.click()
    time.sleep(3)
    error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    print(error_msg.text)
    driver.refresh()
    time.sleep(10)

    driver.quit()



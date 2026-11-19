import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.smoke
@allure.title("verify login")
@allure.description("verify login page")

def test_vwologin():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.find_element(By.NAME,"username").send_keys("aaa")
    driver.find_element(By.NAME,"password").send_keys("ffff")
    driver.find_element(By.ID, "js-login-btn").click()

    WebDriverWait (driver=driver,timeout=10).until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))
    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
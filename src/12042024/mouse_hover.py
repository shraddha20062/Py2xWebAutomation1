import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_mouse_hover():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()

    search=driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']")
    Actions=ActionChains(driver)
    Actions.move_to_element(search).perform()
    time.sleep(10)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_heroku_login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
   # < a
    #id = "btn-make-appointment"
    #href = "./profile.php#login"

    #class ="btn btn-dark btn-lg" > Make Appointment
    #< / a >
    element=driver.find_element(By.ID,"btn-make-appointment")
    element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)
    #< input
    #// *[ @ id = "appointment"] / div / div / div / h2
    username_element = driver.find_element(By.NAME,"username")
    username_element.send_keys("John Doe")
    time.sleep(5)
    password_element = driver.find_element(By.NAME,"password")
    password_element.send_keys("ThisIsNotAPassword")
    submit_button = driver.find_element(By.ID,"btn-login")

    submit_button.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    #// *[ @ id = "appointment"] / div / div / div / h2
    heading = driver.find_element(
        By.XPATH,
        "//section[@id='appointment']//h2"
    )
    assert heading.text == "Make Appointment"

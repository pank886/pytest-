#import requests
from time import sleep
from my_package.common_imports import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.web
def test_web(browser):
    browser.get('http://192.168.1.55:6905/login')

    print(browser.title)

    sleep(3)
    print("查找元素\n")

    username_field = browser.find_element(By.XPATH, '//*[@class="el-input__inner"]')
    password_field = browser.find_element(By.XPATH, '//*[@class="el-input__inner"]')
    login_button = browser.find_element(By.XPATH, '//*[@class="el-button login-btn"]')

    sleep(3)
    print("查找结束\n")

    username_field.send_keys('admin')
    password_field.send_keys('abc12345')


    login_button.click()

    assert "吉大正元智慧园区管理平台" in browser.title
    time.sleep(2)


    pass
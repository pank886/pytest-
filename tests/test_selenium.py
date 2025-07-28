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
    wiit = WebDriverWait(browser, 10)
    print(browser.title)

    username_field = browser.find_element(By.XPATH, '//*[@placeholder="请输入账号"]')
    password_field = browser.find_element(By.XPATH, '//*[@placeholder="请输入密码"]')
    verification_field = browser.find_element(By.XPATH, '//*[@placeholder="请输入验证码"]')
    login_button = browser.find_element(By.XPATH, '//*[@class="el-button login-btn"]')

#自动输入账密
    username_field.send_keys('admin')
    password_field.send_keys('abc12345')
#手动输入验证码
    verification = input("输入验证码：")
    verification_field.send_keys('verification')


    login_button.click()

    assert "吉大正元智慧园区管理平台" in browser.title
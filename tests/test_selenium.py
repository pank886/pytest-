from time import sleep
from my_package.common_imports import *
from selenium import webdriver


@pytest.mark.web
def test_web(browser):
    browser.get('http://192.168.1.55:6905/login')

    print(browser.title)

    username_field = browser.find_element_by_name('username')
    password_field = browser.find_element_by_name('password')
    login_button = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/button')

    username_field.send_keys('admin')
    password_field.send_keys('abc12345')
    login_button.click()

    assert "吉大正元智慧园区管理平台" in browser.title
    time.sleep(2)


    pass
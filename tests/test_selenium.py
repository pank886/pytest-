from my_package.common_imports import *
from selenium import webdriver
from peges.login_page import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.web
def test_web(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login('admin', 'abc12345')

    assert login_page.is_title_contains("吉大正元"), "登录失败，标题错误"

@pytest.mark.web
def test_getRegionList(driver):
    login_page = LoginPage(driver)

    login_ziyuanz = login_page.wait_for_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/nav/div[3]'))

    login_ziyuanz.click()

    assert login_page.wait_for_element((By.XPATH, '//*[@id="bottomElement"]/div[1]/div[2]/span[2]/span[1]/span')), "进入资源中心失败"
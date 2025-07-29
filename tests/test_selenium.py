from my_package.common_imports import *
from selenium import webdriver
from peges.login_page import LoginPage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.mark.web
def test_web(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login('admin', 'abc12345')

    assert login_page.is_title_contains("吉大正元"), "登录失败，标题错误"
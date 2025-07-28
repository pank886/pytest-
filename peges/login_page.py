from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "http://192.168.1.55:6905/login"

    def open(self):
        """打开登录页面"""
        self.driver.get(self.url)

    def get_title(self):
        """获取当前页面标题"""
        return self.driver.title

    def is_title_contains(self, text):
        """判断页面标题是否包含指定文本"""
        return text in self.get_title()

    def wait_for_element(self, locator):
        """等待单个元素出现"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """等待元素可点击"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def login(self, username, password):
        """登录操作"""
        username_field = self.wait_for_element((By.XPATH, '//*[@placeholder="请输入账号"]'))
        password_field = self.wait_for_element((By.XPATH, '//*[@placeholder="请输入密码"]'))
        verification_field = self.wait_for_element((By.XPATH, '//*[@placeholder="请输入验证码"]'))
        login_button = self.wait_for_clickable((By.XPATH, '//*[@class="el-button login-btn"]'))

        username_field.send_keys(username)
        password_field.send_keys(password)
        verification = input("请输入验证码：")
        verification_field.send_keys(verification)

        login_button.click()
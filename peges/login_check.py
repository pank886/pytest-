
# 检查 HTTP 状态码
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

status_code = driver.execute_script("""
    return window.performance.getEntries()[0].responseStatus
""")
if status_code >= 400:
    print(f"页面返回错误状态码: {status_code}")

#捕获 JavaScript 错误
# 在页面加载前设置 JavaScript 错误监听
driver.execute_script("""
    window.errors = [];
    window.onerror = function(message, source, lineno, colno, error) {
        window.errors.push({
            message: message,
            source: source,
            lineno: lineno,
            colno: colno,
            error: error && error.stack
        });
    };
""")

# 加载页面
driver.get("https://example.com")

# 获取捕获的错误
js_errors = driver.execute_script("return window.errors;")
for error in js_errors:
    print(f"JavaScript 错误: {error}")

#检查控制台错误
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 启用浏览器日志
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'browser': 'ALL'}

driver = webdriver.Chrome(desired_capabilities=caps)
driver.get("https://example.com")

# 获取日志
logs = driver.get_log('browser')
for log in logs:
    if log['level'] == 'SEVERE':
        print(f"浏览器控制台错误: {log}")

#检测 404 元素
# 检查常见的 404 提示元素
error_selectors = [
    '.error-404',
    '.error_not_found',
    'h1:contains("404")',
    'body:contains("Page not found")'
]

for selector in error_selectors:
    elements = driver.find_elements_by_css_selector(selector)
    if elements:
        print(f"检测到错误页面元素: {selector}")
        print(f"错误内容: {elements[0].text}")

#检测网络请求失败
# 使用浏览器性能API检测失败的请求
failed_requests = driver.execute_script("""
    return window.performance.getEntries().filter(
        entry => entry.responseStatus >= 400
    );
""")

for req in failed_requests:
    print(f"失败请求: {req.name} - 状态码: {req.responseStatus}")

#检测页面加载超时

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    # 设置页面加载超时
    driver.set_page_load_timeout(10)
    driver.get("https://example.com")
except TimeoutException:
    print("页面加载超时")

# 检查特定元素是否加载
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main-content"))
    )
except TimeoutException:
    print("关键元素加载超时")
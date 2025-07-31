from my_package.common_imports import *

#用例失败时截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs["driver"]
        driver.save_screenshot("fail.png")
import pytest
import requests
from my_package.common_imports import *
from selenium import webdriver
from selenium.webdriver.common.by import By

pytest_plugins = "hooks.report_hooks"


# @pytest.fixture
# def x():
#     print(datetime.datetime.now(), "开始测试")
#     x_1 = {"id" : 1}
#     yield x_1
#     print(datetime.datetime.now(), "结束测试")
#
# @pytest.fixture #依赖于夹具x,返回值是y_1
# def y(x):
#     y_1 = {"Y_id" : x["id"]}
#     yield y_1
#     print("使用了y_1作对比")
#
# @pytest.fixture(scope="session") #scope确定夹具的开始和结束范围，session全局，function函数内
                                 #autouse用于控制某个 fixture 是否自动使用,不要滥用 autouse=True它会让测试变得不透明，难以追踪哪些 fixture 在运行。
                                 # 如果不是所有测试都需要的逻辑，建议保持 autouse=False
def f():
    print(datetime.datetime.now(), "用例开始执行\n")
    yield 3306
    print(datetime.datetime.now(), "用例执行结束\n")

@pytest.fixture(scope='module')
def browser(request):
    deiver = webdriver.Chrome()
    request.node.driver = deiver
    yield deiver
    deiver.quit()

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


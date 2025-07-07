from time import sleep

from my_package.common_imports import *

@pytest.mark.web
def test_web(selenium):
    selenium.get('https://www.baidu.com/')

    print(selenium.title)

    time.sleep(2)
    pass
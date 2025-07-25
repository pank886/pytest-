import os
import pytest
from my_package.common_imports import *

pytest.main()

#自动本地打开测试报告
os.system("allure generate -o report -c temps")

os.system("allure open -h 127.0.0.1 -p 8888 report")
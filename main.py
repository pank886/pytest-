#import os
#import pytest
from my_package.common_imports import *

pytest.main()

os.system("allure generate -o report -c temps")

os.system("allure open -h 127.0.0.1 -p 8888 report")
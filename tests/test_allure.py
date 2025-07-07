from my_package.common_imports import *


@pytest.mark.allure
class TestAllure():
    @allure.epic('园区基线')
    @allure.feature('智慧用水')
    @allure.story('设备管理')
    @allure.title('水量上报')
    def test_weter(self):
        pass
    @allure.epic('园区基线')
    @allure.feature('智慧用电')
    @allure.story('设备管理')
    @allure.title('电量上报')
    def test_uploadElectricity(self):
        pass
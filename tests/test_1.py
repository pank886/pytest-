import pytest

class TestAdd: #测试类

    @pytest.mark.ui
    def test_addition(self, f): #直接以参数形式调用夹具f
        assert 1 + 1 == 2

    @pytest.mark.usefixtures("f") #特殊声明使用夹具f
    @pytest.mark.api
    def test_failure(self):
        assert '1' + '1' == '11' # 这个测试不会失败

    def test_id(self, y):
        assert y["Y_id"] == 1
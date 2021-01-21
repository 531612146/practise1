import pytest
import allure


class Test1():
    # @allure.step(title = "allure.step的title效果展示...")
    @pytest.mark.P0
    def test_case01(self):
        assert 1 == 1

    @pytest.mark.P1
    def test_case02(self):
        assert 1 == 1

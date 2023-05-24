import allure
import pytest

@allure.feature("智能质检系统")
class TestCheck():

    @allure.story("智能质检系统-接口用例")
    @pytest.mark.parametrize("data")
    def test_case_check(self, data):
        print('q111')


if __name__ == "__main__":
    pass
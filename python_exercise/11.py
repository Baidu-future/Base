import unittest
import logging
import requests


class TestSvorderCreate(unittest.TestCase):
    """
    创建问诊服务单接口测试类
    """

    def setUp(self) -> None:
        self.url = config.get_test_host(__class__.__name__)
        if not self.url:
            logging.fatal('get test host failed')
        return super().setUp()

    def tearDown(self) -> None:
        self.url = ""
        return super().tearDown()

    def test_order_create_success_0(self):
        """
        @description: 测试正常创建订单 0 定向非拇指
        @param {*}
        @return {*}
        """
        req = dataHandler.build_create_paramas(0)
        headers = dataHandler.get_headers()
        res = requests.post(self.url, json=req, headers=headers)
        data = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 0)

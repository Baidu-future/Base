import unittest
from BeautifulReport import BeautifulReport


class UnittestCaseSecond(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""

    def test_equal(self):
        """
        test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)

    @BeautifulReport.add_test_img('测试报告.png')
    def test_is_none(self):
        """
        test None object
        :return:
        """

        self.assertIsNone(None)
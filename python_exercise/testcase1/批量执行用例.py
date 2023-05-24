import unittest
from  testcase1 import test_jifa
from HtmlTestRunner import HTMLTestRunner

# 生成测试套件
path= "//testcase1"
s = unittest.defaultTestLoader.discover(path, "test*.py")
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test_jifa.Test_01))
runner = HTMLTestRunner(output="/Users/v_yuanliangliang/Desktop")
runner.run(suite)

# 以只写方式打开测试报告文件
# f = open("/Users/v_yuanliangliang/Desktop/000.html", "wb")
# # 实例化 HTMLTestRunner 对象  stream：open 函数打开的文件流； title：[可选参数]，为报告标题； description：[可选参数]，为报告描述信息；比如操作系统、浏览器等版本；
# runner = HtmlTestRunner.HTMLTestRunner(stream=f)
#
# # 执行
# runner.run(suite)


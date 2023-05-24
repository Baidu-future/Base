import hashlib
import unittest

# def get_sha256(obj):
#     # 1-1实例化加密对象
#     sha256=hashlib.sha256()
#     # 1-2进行加密
#     sha256.update(obj.encode('utf-8'))
#     # 1-3返回加密后的结果
#     return sha256.hexdigest()
# print(get_sha256('111111'))
# #bcb15f821479b4d5772bd0ca866c00ad5f926e3580720659cc80d39c9d09802a

if __name__=="__main__":
    suite = unittest.TestLoader().discover("./", "*.py")
    # 以只写方式打开测试报告文件
    f = open("./wz_SDK_unify.py", "w", encoding="utf-8")
    # 实例化TextTestRunner stream为open函数打开的文件流； verbosity 为不同模板编号
    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    # 执行
    runner.run(suite)
    # 关闭
    f.close()
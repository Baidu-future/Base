import hashlib
import logging
logging.basicConfig(filename='e.log', level=logging.DEBUG)
def get_md5(obj):
    # 实例化加密对象
    md5=hashlib.md5()
    # 进行加密操作
    md5.update(obj.encode('utf-8'))
    # 返回加密后的结果
    return md5.hexdigest()
print(get_md5('1113331'))
# 96e79218965eb72c92a549dd5a330112

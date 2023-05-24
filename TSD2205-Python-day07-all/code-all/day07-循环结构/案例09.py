"""
案例09:使用for循环,循环输出2维列表中的数据
"""
cases = [
    ['login_01', 'admin', '123456', True],
    ['login_02', 'admin', '654321', False],
    ['login_03', 'root', '123456',  False]
]
for case in cases:                  # 循环
    print(case)
    uid, uname, pwd, res = case     # 解包
    print(res)
    if res:                         # 判断
        print('测试用例执行成功')
    else:
        print('测试用例执行失败')


# 练习02:使用while循环,循环输入数据,并输出结果,当输入的数据中包含(含有)q时,
# 退出循环
while True:
    str01 = input('请输入数据:')
    print(str01)
    if 'q' in str01:
        break


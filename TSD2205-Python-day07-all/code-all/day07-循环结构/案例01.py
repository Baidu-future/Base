# 描述:while循环
i = 1            # 循环变量初值
while i < 5:     # 循环条件
    print('Hello World')
    i = i + 1    # 循环变量增值
# 解析
"""
i = 1   1 < 5    True    Hello World    i = 1 + 1   
i = 2   2 < 5    True    Hello World    i = 2 + 1
i = 3   3 < 5    True    Hello World    i = 3 + 1
i = 4   4 < 5    True    Hello World    i = 4 + 1
i = 5   5 < 5    False
"""
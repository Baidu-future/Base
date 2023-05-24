"""
练习07:使用for循环,输出列表中的元素,将元素首字母变成大写,其余字母变成小写显示
zhangsan  ---->  Zhangsan
"""
list01 = ['zhangsan', 'LISI', 'wangWu', 'ZhaoLiU', 'tianQi']
list02 = []
print('修改前元素:', list01)
# 获取列表中的元素
for k in list01:
    # 将元素首字母变大写,其余字母小写   切片 切段  连接
    w1 = k[0].upper()
    w2 = k[1:].lower()
    w3 = w1 + w2
    # 将修改完的元素,存入list02列表中
    list02.append(w3)
# 输出liest02列表
print('修改后元素:', list02)

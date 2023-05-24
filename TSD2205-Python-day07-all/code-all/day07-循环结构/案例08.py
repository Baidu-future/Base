# 案例08:使用for循环,输出字典中的元素
dict01 = {'id':101, 'name':'张三', 'age':20}

for k, v in dict01.items():   # items()  以键值对形式显示
    print(k, v)

for v in dict01.values():     # values()  获取字典中的全部值
    print(v)

for k in dict01.keys():         # keys()    获取字典中的全部键
    print(k)

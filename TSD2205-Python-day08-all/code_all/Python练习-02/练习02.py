# 练习2、创建2个列表 list1和list2,
list1 = [11, 22, 33, 44, 55, 66, 77, 'test']
list2 = ['rose', '女', 'BJ', 30, 'tom', '男', 'BJ', 25]
# (1)定义一个变量list3,获取list1+list2的值,输出list3
list3 = list1 + list2
print(list3)
# (2)向list1列表尾部追加一个元素: 88,输出列表最新元素
list1.append(88)
print(list1)
# (3)计算list2中'BJ'出现的次数,并输出
count = list2.count('BJ')
print('出现的次数:', count)
# (4)删除list1列表中,'test'元素, 输出列表最新元素
list1.pop(-2)
print(list1)
# (5)对list1列表进行由大到小降序排列
list1.sort(reverse=True)
# sort()  表示排序  默认是升序   降序设置 reverse=True
print(list1)

list3 = list1[::-1]
print(list3)
# (6)计算list1列表中,元素的最大值,最小值,元素之和,及元素个数,一条输出语句显示
print(max(list1),min(list1),sum(list1),len(list1))




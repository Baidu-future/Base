# 描述:字典常见函数
# len()
dict01 = {'A':100, 'B':200, 'C':300}
len = len(dict01)
print('字典中元素的个数是:%d' % len)

# keys()
dict02 = {'A':100, 'B':200, 'C':300}
keys = dict02.keys()
print('字典中全部的键:', keys)

# values()
dict03 = {'A':100, 'B':200, 'C':300}
values = dict02.values()
print('字典中全部的值:', values)

# get()
dict04 = {'A':100, 'B':200, 'C':300}
values = dict04.get('B')
print('键对应的值是:', values)

# items()
dict05 = {'A':100, 'B':200, 'C':300}
key_values = dict05.items()
print('键值形式显示:', key_values)

# pop()
dict06 = {'A':100, 'B':200, 'C':300}
print('删除前字典元素:', dict06)
values = dict06.pop('C')
print('删除后字典元素:', dict06)
print('字典中删除键对应的值是:', values)

# update()
dict07 = {'id':101, 'name':'mary', 'age':20}
dict08 = {'A':100, 'B':200, 'id':101, 'age':30}
dict07.update(dict08)
print('新字典元素是:', dict07)


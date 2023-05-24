# 描述:字典(dict)

# 定义字典
dict01 = {'id':101, 'name':'rose', 'age':20, 'address':'北京市朝阳区'}
dict02 = dict(id=101, name='rose', age=20, address='北京市朝阳区')

# 使用字典
# 通过字典名访问
print(dict01)
print(dict02)
# 通过字典名+键访问
print(dict01['address'])
print(dict02['name'])
# 解包
d1, d2, d3, d4 = dict01
print(d4)

# 猜答案
cases = [
    {'id':'case_01', 'name':'admin', 'passwd':123456, 'status':True},
    {'id':'case_02', 'name':'root', 'passwd':'abc123', 'status':False}
]
print(cases[1]['passwd'])

# 特殊情况的字典
# 空字典
d5 = {}
d6 = dict()
# 无名字典
dict()


# 删除字典
# 通过字典名删除
del dict01
# print(dict01)
# NameError: name 'dict01' is not defined

# 通过字典名+键删除
print('原字典元素:', dict02)
del dict02['name']
print('删除后字典元素:', dict02)


# 增加和修改字典元素
dict03 = {'A':100, 'B':200, 'C':300}
print('原字典元素:', dict03)
# 增加元素
dict03['D'] = 400
print('增加后字典元素:', dict03)
# 修改元素
dict03['B'] = 500
print('修改后字典元素:', dict03)


# 类型转换
# 字典转换字符串
dict04 = {'name':'rose', 'age':20, 'sal':7000}
str01 = '%(name)s%(age)d%(sal)d' % dict04
print(dict04, type(dict04))
print(str01, type(str01))

# 字符串转字典
str02 = "{'name':'rose', 'age':20, 'sal':7000}"
dict05 = eval(str02)
print(str02, type(str02))
print(dict05, type(dict05))


# 列表转字典
list01 = [
           ['name', 'rose'],
           ['age', 20],
           ['sal', 9000]
]
dict06 = dict(list01)
print(dict06, type(dict06))

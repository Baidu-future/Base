# 练习3、创建1个元组,元组名为car
car = ('法拉利', 2000000, '红色', 'rose', 25, '北京')
# (1)通过2种方式输出,元组全部成员
print(car)
print(car[0],car[1],car[2],car[3],car[4])
c1, c2, c3, c4, c5, c6 = car
print(c1, c2, c3, c4, c5, c6 )
# (2)删除元组car并验证
del car
# print(car)
# NameError: name 'car' is not defined

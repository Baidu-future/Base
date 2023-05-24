# 案例02:运行时异常错误

emp_list = [101, 'rose', 20]
del emp_list
print(emp_list)
# NameError: name 'emp_list' is not defined

print(emp_list[5])
# IndexError: list index out of range

num = int(input('请输入您的数据:'))
print('您的数值是:%d' % num)
# ValueError: invalid literal for int() with base 10: 'dsfd'

n1 = 'Python'
n2 = 100
res = n1 + n2
print(res)
# TypeError: can only concatenate str (not "int") to str

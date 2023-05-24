"""
简易计算器(加、减、乘、除) V1.2
"""
num1 = float(input('请输入第1个数:'))
num2 = float(input('请输入第2个数:'))

# print(num1, type(num1))   # '100' --->  100   str -- int(float)
# print(num2, type(num2))

# 加法(add)
add_res = num1 + num2
# print(add_res)    100 + 200 = 300
print(num1, '+', num2, '=', add_res)

# 减法(sub)
sub_res = num1 - num2
# print(sub_res)
print(num1, '-', num2, '=', sub_res)

# 乘法(mul)
mul_res = num1 * num2
# print(mul_res)
print(num1, '*', num2, '=', mul_res)

# 除法(div)
div_res = num1 / num2
# print(div_res)
print(num1, '/', num2, '=', div_res)

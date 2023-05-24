"""
练习1、获取用户键盘输入的整数值,存入变量num1中,获取用户键盘输入的整数值,
存入变量num2中,然后交换A和B两个变量的值,并输出
"""
num1 = int(input('请输入第1个数:'))
num2 = int(input('请输入第2个数:'))
print('交换前:', num1, num2)
print('-----------------------')
# print('交换后:', num2, num1)   # 方法-1

# num1, num2 = num2, num1       # 方法-2
# print('交换后:', num1, num2)

# 方法-3
temp = num1
num1 = num2
num2 = temp
print('交换后:', num1, num2)



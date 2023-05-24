# 描述:字符串-格式化字符
x = 3.14
y = 2.56
z = x + y
print(z)
print('%f+%f=%f' % (x, y, z))
print('%.2f+%.2f=%.2f' % (x, y, z))  # .2f 表示保留2位小数


# %c
sex = input('请输入您的性别:')
print('您的性别是:%c' % sex)
# %e
a = 9
b = 2
print(b ** a)
print('b^a=%e' % b ** a)
print('b^a=%.2e' % b ** a)
print('%d^%d=%.2e' % (b, a, b ** a))
# %%
g = 85
print('%d%%' % g)



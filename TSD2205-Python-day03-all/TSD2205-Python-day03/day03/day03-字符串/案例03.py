# 描述:字符串-格式化字符
x = int(input('请输入第1个数:'))
y = int(input('请输入第2个数:'))
z = x + y
# 要求输出 100 + 200 = 300 这样的样式
print(x, '+', y, '=', z)              # 方法-1
print('%d+%d=%d' % (x, y, z))         # 方法-2
print(f'{x}+{y}={z}')                 # 方法-3

print(f'{x}*{y}={x*y}')

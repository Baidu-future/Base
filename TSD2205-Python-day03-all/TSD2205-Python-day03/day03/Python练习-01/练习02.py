"""
练习2、获取用户键盘输入的分钟数,存入变量M,获取用户输入的小时数,存入变量H,
计算M分钟+H小时是多少秒S,并输出
"""
#   H       M         S
# 1小时 = 60分钟 = 3600秒
H = int(input('请输入小时数:'))
M = int(input('请输入分钟数:'))
S = H * 3600 + M * 60
print(S)
print('总秒数是:', S)
# 1小时1分钟是:3660秒
print(H, '小时', M, '分钟是:', S, '秒')
print('%d小时%d分钟是:%d秒' % (H, M, S))








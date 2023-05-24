# 描述:字符串解包和比较
str01 = 'ABCD'

s1, s2, s3, s4 = str01     # 解包
print('第1个字符是:', s1)
print('第4个字符是:', s4)

str02 = 'HELLO'
print(str02)    # H-E-L-L-O
s5, s6, s7, s8, s9 = str02
print(s5, s6, s7, s8, s9, sep='-')

str03 = '15510593333'  # --> 155-1059-3332
s01 = str03[:3]
s02 = str03[3:7]
s03 = str03[7:]
print(s01, s02, s03, sep='-')

str04 = 'rose'
str05 = 'rose'
str06 = 'Rose'
print(str04 == str05)   # True
print(str05 == str06)   # False
# 预期结果和实际结果是否相等  判断是否是缺陷






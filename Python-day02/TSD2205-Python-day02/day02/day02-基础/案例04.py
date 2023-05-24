# 描述:逻辑运算符
a = -30
b = -50

res1 = a < 0 and b < 0
print(res1)             # True

# A = B  B = C  --->  A = C

res2 = a < 0 and b > 0
print(res2)             # False
# print(a < 0 and b > 0)

print(a < 0 and 1/2)    # 0.5      # -30 < 0  True
print(a > 0 and 1/2)    # False    # -30 > 0  False  短路重点
print('---------------------------------------------------')

print(a > 0 or b < 0)   # -30 > 0  or -50 < 0   True
print(a < 0 or b < 0)   # -30 < 0  or -50 < 0   True

print(a > 0 or b > 0)   # -30 > 0  or -50 > 0   False
print(a < 0 or 1/2)     # -30 < 0  or 1/2       True    短路重点

print(not a < 0)        # -30 < 0   False









# 案例06:使用while循环,输出1--10内偶数相加之和
i = 1
sum1 = 0
while i <= 10:
    if i % 2 == 0:     # i % 2 == 0    判断是否是偶数
        sum1 = sum1 + i
    i = i + 1
print(sum1)


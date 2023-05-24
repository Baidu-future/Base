# 练习01:使用for循环,循环输出1+2+3+4+...+99+100的和,当和大于3000时,退出循环
sum1 = 0
for k in range(1, 101):
    sum1 = sum1 + k
    if sum1 > 3000:
        break
print('1--100之和:', sum1)

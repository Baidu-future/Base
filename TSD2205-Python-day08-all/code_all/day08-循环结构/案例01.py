# 案例01:运动员操场跑圈   10

# while
i = 1
while i <= 10:
    print('小明跑第%d圈' % i)
    i = i + 1
    if i == 5:
        break


# for
for k in range(1,11):
    if k == 5:
        break
    print('小花跑第%d圈' % k)
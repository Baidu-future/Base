# 练习04:使用循环输出1-10内的奇数
# 1   3   5   7   9

# while
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i = i + 2

# for
# for k in range(1,11,2):
#     print(k)

# continue
for y in range(1,11):
    if y % 2 == 0:
        continue
    print(y)

# i = 0
# while i < 10:
#     i = i + 1
#     if i % 2 == 0:
#         continue
#     print(i)


# 练习1、定义一个字符串变量str1,赋值为"abcde,HelloJava,GoodByeABCDE",
str1 = "abcde,HelloJava,GoodByeABCDE"
# (1)计算字符串str1的长度
len = len(str1)
print('字符串长度是:', len)
# (2)查询字母o在字符串中出现的次数
count = str1.count('o')
print('字母o在字符串中出现的次数:', count)
# (3)将字符串使用分隔符(,)分多个字符串
list01 = str1.split(',')
print(list01)
# (4)将字符串全部字母变成小写显示
str01 = str1.lower()
print('小写显示:', str01)
# (5)使用Python替换字符串str1中Java
str02 = str1.replace('Java','Python')
print('新字符串:',str02)
# (6)判断字符串是否全部都是字母,如果全部都是,提出提示信息
res1 = str1.isalpha()
print(res1)
# (7)判断Python字符串是否包含在字符串str1中,并输出结果
res2 = 'Python' in str1
print(res2)


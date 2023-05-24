"""
练习1、获取键盘输入的月份,赋值给变量month,输出该月份所属的季节,提示:3,4,5 春季
6,7,8 夏季  9,10,11 秋季 12, 1, 2 冬季
"""
month = int(input('请输入月份:'))
# if month == 3 or month == 4 or month == 5:
if month in (3,4,5):
    print(month,'月是春季')
elif month == 6 or month == 7 or month == 8:
    print(month,'月是夏季')
elif month == 9 or month == 10 or month == 11:
    print(month,'月是秋季')
elif month == 12 or month == 1 or month == 2:
    print(month,'月是冬季')


"""
练习4、获取键盘输入的年份,赋值给变量year,并判断1000~5000年之间,那些是平年那些闰年,
如果输入错误年份,给出错误信息提示, 获取键盘输入的月份,赋值给变量month,并判断是否在
1---12月之间,如果在,判断每个月的天数,如果不在给出错误信息提示
"""
year = int(input('请输入年份:'))
if 5000 >= year >= 1000:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year,'是闰年')
        month = int(input('请输入月份:'))
        if 12 >= month >= 1:
            if month in (1, 3, 5, 7, 8, 10, 12):
                print(month, '月是31天')
            elif month in (4, 6, 9, 11):
                print(month, '月是30天')
            else:
                print(month, '月是29天')
        else:
            print('您输入的月份有误,请重新输入')
    else:
        print(year, '是平年')
        month = int(input('请输入月份:'))
        if 12 >= month >= 1:
            if month in (1, 3, 5, 7, 8, 10, 12):
                print(month, '月是31天')
            elif month in (4, 6, 9, 11):
                print(month, '月是30天')
            else:
                print(month, '月是28天')
        else:
            print('您输入的月份有误,请重新输入')
else:
    print('您输入的年份有误,请重新输入')


# month = int(input('请输入月份:'))
# if 12 >= month >= 1:
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         print(month, '月是31天')
#     elif month in (4, 6, 9, 11):
#         print(month, '月是30天')
#     else:
#         print(month, '月是28/29天')
# else:
#     print('您输入的月份有误,请重新输入')
"""
练习01:简易计算器(加、减、乘、除) V3.2
1)流程控制语句
2)while循环
"""
while True:
    print('|===========================|')
    print('|\t\t\t计算器\t\t\t|')
    print('|===========================|')
    num1 = float(input('| 请输入第1个数:'))
    sym = input('| 请输入计算符号:')
    num2 = float(input('| 请输入第2个数:'))
    if '+' == sym:
        # 加法(add)
        add_res = num1 + num2
        print('|', num1, '+', num2, '=', add_res)
    elif '-' == sym:
        # 减法(sub)
        sub_res = num1 - num2
        print('|', num1, '-', num2, '=', sub_res)
    elif '*' == sym:
        # 乘法(mul)
        mul_res = num1 * num2
        print('|', num1, '*', num2, '=', mul_res)
    elif '/' == sym:
        if num2 != 0:
            # 除法(div)
            div_res = num1 / num2
            print('|', num1, '/', num2, '=', div_res)
        else:
            print('| 提示:除数不能为零')
    else:
        print('| 提示:功能未实现,持续更新中....')
    print('|===========Bey-Bey=========|')




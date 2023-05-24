"""
练习01:简易计算器(加、减、乘、除) V4.3
要求:
输入和输出函数应用
类型转换
格式化字符
运算符
流程控制语句
异常处理
"""
while True:
    print('|===========================|')
    print('|\t\t\t计算器\t\t\t|')
    print('|===========================|')
    try:
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
        elif 'q' == sym:
            break
        else:
            print('| 提示:功能未实现,持续更新中....')
    except:
        print('| 提示:您输入的数据有误!')
print('|===========Bey-Bey=========|')
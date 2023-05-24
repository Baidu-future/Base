# 案例03:获取键盘输入的数据,发生异常,进行异常处理
while True:
    try:
        num1 = int(input('请输入第1个数:'))
        num2 = int(input('请输入第2个数:'))
        res = num1 + num2
        print(f'{num1}+{num2}={res}')
    except:
        print('您输入的数据无效,请重新输入')





"""
练习3、获取用户键盘输入的体重(千克),存入变量weight,获取用户输入的身高(米),
存入变量height,计算BMI值,并输出(公式:BMI=体重(千克)除以身高(米)的平方)
"""
weight = float(input('请输入您的体重:'))
height = float(input('请输入您的身高:'))
BMI = weight / (height * height)
print('BMI=',BMI)


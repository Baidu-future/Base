"""
练习4、获取用户键盘输入的用户名,存入变量username,获取用户键盘输入的密码,
存入变量passwd,获取用户键盘输入的验证码,存入变量captcha,并输出
"""
username = input('请输入您的用户名:')
passwd = input('请输入您的密码:')
captcha = input('请输入您的验证码:')
print(username, passwd, captcha)
print(username, passwd, captcha, sep='-')
print('username=', username, 'passwd=', passwd, 'captcha=', captcha)
print('username=%s passwd=%s captcha=%s' % (username, passwd, captcha))

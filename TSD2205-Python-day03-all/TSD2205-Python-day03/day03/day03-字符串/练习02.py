# 描述:用户登录问题
"""
(1)获取键盘输入的用户名(uname)、密码(passwd)、验证码(cap)
(2)假设 用户名:admin   密码:abc123   验证码:Ab15
(3)验证码不分区大小写
(4)登录成功-True  登录失败-False
"""
uname = input('请输入用户名:')
passwd = input('请输入密码:')
cap = input('请输入验证码:')
# print(uname, passwd, cap)
cap = cap.upper()
print(uname == 'admin' and passwd == 'abc123' and cap == 'AB15')

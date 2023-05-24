"""
描述:  编写用户注册代码
逻辑:  界面 ---> 界面中输入的数据到数据库中 ---> 验证
模拟: input -->     2维列表中            ---> 输出
      uname                                 print()
      passwd
"""

# 用户界面
print('====================')
uname = input('请输入注册的用户名:')
passwd = input('请输入注册的密码:')
print('注册成功')
print('====================')
# 存储用户数据的列表
users_list = []
# 自己设计的字典数据
info01 = {'uname':uname, 'passwd':passwd}
# 自己设计的列表数据
info02 = [uname, passwd]
# 添加数据到列表中
users_list.append(info02)
# 验证
print(users_list)

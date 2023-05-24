"""
练习6、使用列表实现简单的用户登录功能,创建2个列表分别存储用户名(uname)
和密码(passwd)使用for循环,循环输入数据,并进行验证
例如:
uname = ['root','admin','rose']
passwd =['123','456','789']
说明:当用户键盘输入root和密码123时,提示登录成功,否则失败,用户名和密码是对应关系
"""
# while True:
for i in range(3):
    # 列表中存储的用户名和密码    相当于数据库
    uname = ['root','admin','rose']
    passwd = ['123','456','789']
    # 获取键盘输入用户名和密码
    name = input('请输入用户名:')
    if name in uname:   # 判断输入的用户名是否包含在uname列表中
        # 获取输入的用户名在uname列表中的,下标
        name_index = uname.index(name)
        # 输入密码
        pwd = input('请输入密码:')
        if passwd[name_index] == pwd:
        # 获取passwd列表中的密码   用户输入的密码
            print('登录成功')
            break
        else:
            print('密码错误')
    else:
        print('用户名不存在')



# # 输入的用户名和密码和列表中的用户名和密码比较   算法
# if 'root' == name and '123' == pwd:
#     # 如果相同,提示登录成功
#     print('登录成功')
#     # 否则登录失败
# else:
#     print('用户名或密码错误')






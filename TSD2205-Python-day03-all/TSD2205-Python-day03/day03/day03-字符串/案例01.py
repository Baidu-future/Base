# 描述:字符串-格式化字符
name = input('请输入您的姓名:')
print('您输入的姓名是:', name)
print('您输入的姓名是:%s' % name)

address = input('请输入您的地址:')
print('您输入的地址是:%s' % address)
print('您输入的姓名是:%s,您输入的地址是:%s' % (name, address))

sal = int(input('请输入您的工资:'))
print('您输入的工资是:%d' % sal)

print('您的姓名是:%s,您的地址是:%s,您的工资是:%d' %(name, address, sal))
# 练习4、创建1个字典,字典名为stu1
stu1 = {'sid':1001,'sname': 'jack', 'age':22, 'sex': '男',
       'address': '北京'}
# (1)复制字典stu1,赋值给变量stu2,并输出
stu2 = stu1.copy()
print(stu2)
# (2)以'键:值'形式返回字典stu1中的元素,并输出
kv = stu1.items()
print(kv)
# (3)删除'键'是address的元素
del stu1['address']
print(stu1)



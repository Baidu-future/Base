"""
切片练习:获取键盘输入的18位身份证号码,输出身份证中的省区县、出生年月日
# 110201-19831027-2351
"""
sfz = input('请输入您的身份证号码:')
print('省区县号码是:', sfz[:6])
print('出生年月日:', sfz[6:14])


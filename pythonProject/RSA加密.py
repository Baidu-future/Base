import    rsa
import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 开始使用log功能
logging.info('这是 loggging info message')
logging.debug('这是 loggging debug message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')

def get_rsa(obj):
    #1-1 实例化加密对象
    (pubkey,privkey)=rsa.newkeys(1024)
    #1-2 公钥加密1
    pwd1=rsa.encrypt(str.encode('utf-8'),pubkey)
    print('加密后结果1为：',pwd1.hex())
    #1-3 私钥解密1
    depwd1=rsa.decrypt(pwd1,privkey)
    print('解密后的结果1为：',depwd1.decode())
get_rsa('111111')
# 加密后结果1为： 5be88fe6e17fd4286eec97f6ac528682b8a709a359c16545c0a1c692480c74471175241a4f3396792621930d773628b4443fcb790470d92fbb4511d51e5621ca737473d0c8d91c58276370f46103fdcfd2adefb697a60b0ed10ca68e0b015ad7f9584e3067ecd40cd3009d6d6bf5b98873880f12a88244e09f707a00b9e47f53
# 解密后的结果1为： utf-8

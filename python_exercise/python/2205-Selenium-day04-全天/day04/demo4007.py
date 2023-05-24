from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('http://localhost/upload/user.php')#打开登录页
sleep(3)
driver.find_element(By.NAME,'submit').click()#点击“立即登陆”
sleep(3)
a1=driver.switch_to.alert#切换到消息框
t1=a1.text#获得消息框里的消息文本
print(t1)
a1.accept()#点击“确定”按钮
sleep(5)
driver.quit()
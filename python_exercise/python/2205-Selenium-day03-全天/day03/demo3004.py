from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/message.php')#打开留言板页
# 定位留言类型的一组单选按钮
# a=driver.find_elements(By.NAME,'msg_type')
# print(type(a))#<class 'list'>
# 点击留言类型的一组单选按钮中第3个
driver.find_elements(By.NAME,'msg_type')[2].click()

# 循环点击留言类型的一组单选按钮
for e in driver.find_elements(By.NAME,'msg_type'):
    e.click()
    sleep(1)

driver.find_elements(By.NAME,'msg_type123')[0].click()

sleep(4)
driver.quit()
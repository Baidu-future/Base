from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/message.php')#打开留言板页
driver.find_element(By.NAME,'msg_content').send_keys('hello\n你好')
# 练习：清空该文本域，输入三行信息，第一行“我是学生”，第二行“达内的学生”，第三行“达内软件测试的学生”
driver.find_element(By.NAME,'msg_content').clear()
driver.find_element(By.NAME,'msg_content').send_keys('我是学生\n达内的学生\n达内软件测试的学生')
sleep(4)
driver.quit()
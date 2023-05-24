from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()#启动Firefox
driver.get('http://localhost/upload/index.php')#打开ECShop前台首页
driver.find_element(By.LINK_TEXT,'留言板').click()#点击“留言板”
sleep(3)#等待3秒
driver.find_element(By.NAME,'user_email').send_keys('jack@126.com')#输入电子邮件地址：jack@126.com
driver.find_element(By.NAME,'msg_title').send_keys('hello')#输入主题：hello
driver.find_element(By.NAME,'msg_content').send_keys('你好')#输入留言内容：你好
driver.find_element(By.TAG_NAME,'textarea').send_keys('789')#演示TAG_NAME
driver.find_element(By.XPATH,'//textarea').send_keys('456')
sleep(3)#等待3秒
driver.find_element(By.CLASS_NAME,'bnt_blue_1').click()#点击“我要留言”按钮
sleep(5)#等待5秒
driver.quit()#关闭浏览器
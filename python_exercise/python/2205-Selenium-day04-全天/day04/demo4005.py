from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get('http://localhost/upload/user.php')#打开登录页
driver.find_element(By.NAME,'username').send_keys('vip')#输入用户名vip
driver.find_element(By.NAME,'password').send_keys('vip')#输入密码vip
driver.find_element(By.NAME,'submit').click()#点击“立即登陆”
sleep(5)#注意：不要等待3秒左右（因为3秒时，网页正在自动跳转）
driver.find_element(By.LINK_TEXT,'用户中心').click()
sleep(4)
driver.find_element(By.PARTIAL_LINK_TEXT,'我的留言').click()
sleep(4)
driver.find_element(By.NAME,'msg_title').send_keys('111')#输入主题111
driver.find_element(By.NAME,'msg_content').send_keys('222')#输入留言内容222
driver.find_element(By.NAME,'message_img').send_keys('D:\\1.txt')#浏览选择一个文件，参数是文件的绝对路径（str类型）
driver.find_element(By.CLASS_NAME,'bnt_bonus').click()#点击“提交”
sleep(6)
driver.quit()
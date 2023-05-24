from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get('http://localhost/upload/user.php')#打开登录页
driver.find_element(By.NAME,'username').send_keys('vip')#输入用户名vip
sleep(2)
driver.find_element(By.NAME,'username').send_keys(Keys.CONTROL,'a')#对用户名文本框输入组合键Ctrl+a  全选
driver.find_element(By.NAME,'username').send_keys(Keys.CONTROL,'c')#对用户名文本框输入组合键Ctrl+c  复制
driver.find_element(By.NAME,'password').send_keys(Keys.CONTROL,'v')#对密码文本框输入组合键Ctrl+v   粘贴
driver.find_element(By.NAME,'password').send_keys(Keys.ENTER)#在密码文本框里按下回车ENTER  进行登陆操作  登录成功
sleep(5)

driver.find_element(By.LINK_TEXT,'留言板').click()# 练习：点击“留言板”，
sleep(3)# 等待3秒，
driver.find_element(By.NAME,'user_email').send_keys(Keys.CONTROL,'a')# 对电子邮件地址文本框输入组合键Ctrl+a全选、
driver.find_element(By.NAME,'user_email').send_keys(Keys.CONTROL,'c')# 输入组合键Ctrl+c复制，
driver.find_element(By.NAME,'msg_title').send_keys(Keys.CONTROL,'v')# 对主题文本框输入组合键Ctrl+v粘贴，
driver.find_element(By.NAME,'msg_content').send_keys(Keys.CONTROL,'v')# 对留言内容文本域输入组合键Ctrl+v粘贴，
driver.find_element(By.NAME,'msg_title').send_keys(Keys.ENTER)# 对主题文本框输入回车键提交。

sleep(5)
driver.quit()
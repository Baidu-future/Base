from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/admin/index.php')#打开后台页
driver.find_element(By.NAME,'username').send_keys('admin')#输入正确用户名
driver.find_element(By.NAME,'password').send_keys('admin123')#输入正确密码
driver.find_element(By.NAME,'captcha').send_keys('0')#输入万能验证码
driver.find_element(By.CLASS_NAME,'button').click()#点击“进入管理中心”按钮
sleep(9)
f1=driver.find_element(By.XPATH,"//frame[contains(@src,'top')]")
driver.switch_to.frame(f1)
driver.find_element(By.LINK_TEXT,'开店向导').click()
sleep(5)
driver.quit()
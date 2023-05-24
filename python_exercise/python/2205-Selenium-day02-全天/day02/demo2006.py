from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()#启动Firefox
driver.get('http://localhost/upload/message.php')#打开留言板页
driver.find_element(By.XPATH,'//form/a').click()#点击高级搜索
sleep(2)
driver.find_element(By.XPATH,'//form/input[1]').send_keys('a')#输入a
driver.find_element(By.XPATH,'//form/input[2]').click()#点击“搜索”
sleep(5)
driver.find_element(By.XPATH,'//font/a[1]/img').click()#点击“登录”
sleep(3)
driver.find_element(By.XPATH,'//font/a[2]/img').click()# 练习：点击“注册”
sleep(3)
driver.find_element(By.XPATH,'//a[@name="top"]/img').click()#点击左上角ECSHOP商标（可以回到首页）
sleep(3)
driver.find_element(By.XPATH,'//a[@href="pick_out.php"]').click()#点击选购中心
sleep(2)
driver.quit()
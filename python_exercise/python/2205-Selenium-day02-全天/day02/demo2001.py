from selenium import webdriver
from selenium.webdriver.common.by import By#导入定位专用类
driver=webdriver.Firefox()#启动浏览器
driver.get('http://localhost/upload/user.php?act=register')#打开ECShop前台注册页
driver.find_element(By.ID,'username').send_keys('123')#向用户名文本框里输入123
driver.find_element(By.ID,'email').send_keys('456')#向email文本框里输入456
driver.find_element(By.ID,'password1').send_keys('789')#输入密码789
driver.find_element(By.NAME,'extend_field1').send_keys('111')#输入MSN 111
driver.find_element(By.NAME,'agreement').click()#点击复选框
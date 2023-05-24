from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()#启动浏览器
driver.get('http://localhost/upload/index.php')#打开前台首页
driver.find_element(By.NAME,'order_sn').send_keys('2009061909851')#输入有效的订单号
driver.find_element(By.CLASS_NAME,'bnt_blue_2').click()#点击“查询该订单号”按钮
sleep(5)
driver.quit()#关闭浏览器

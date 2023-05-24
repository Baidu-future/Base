from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/index.php')#打开前台首页
k=driver.find_element(By.ID,'keyword')#定位元素
k.send_keys('a')
sleep(2)
k.send_keys('b')
sleep(2)
# driver.refresh()#刷新当前网页
driver.find_element(By.NAME,'imageField').click()#点击搜索
# k=driver.find_element(By.ID,'keyword')#定位元素
k.send_keys('c')
sleep(2)
k.send_keys('d')
sleep(4)
driver.quit()
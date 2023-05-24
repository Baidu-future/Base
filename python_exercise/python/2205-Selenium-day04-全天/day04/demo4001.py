from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get('http://localhost/upload/index.php')#打开首页
driver.find_element(By.ID,'keyword').send_keys('806')#搜索关键词806
driver.find_element(By.NAME,'imageField').click()#点击搜索
sleep(3)
driver.find_element(By.ID,'keyword').clear()#清空
driver.find_element(By.ID,'keyword').send_keys('810')#搜索关键词810
driver.find_element(By.ID,'keyword').send_keys(Keys.ENTER)#输入回车
sleep(3)
driver.quit()
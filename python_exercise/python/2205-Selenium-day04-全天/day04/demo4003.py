from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get('http://localhost/upload/index.php')#打开首页
driver.find_element(By.ID,'keyword').send_keys('806')#搜索关键词806
driver.find_element(By.NAME,'imageField').click()#点击搜索
sleep(3)
driver.find_element(By.ID,'keyword').click()#点击文本框
sleep(1)
driver.find_element(By.ID,'keyword').send_keys(Keys.END)#结束，光标移动到末尾
sleep(1)
driver.find_element(By.ID,'keyword').send_keys(Keys.BACKSPACE)#删除6
sleep(1)
driver.find_element(By.ID,'keyword').send_keys(Keys.BACKSPACE)#删除0
sleep(1)
driver.find_element(By.ID,'keyword').send_keys('10')#搜索关键词10
sleep(1)
driver.find_element(By.ID,'keyword').send_keys(Keys.ENTER)#输入回车
sleep(3)
driver.quit()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/index.php')#打开首页
driver.find_element(By.XPATH,'//*[@id="keyword"]').send_keys('a')#输入关键字a
driver.find_element(By.XPATH,'//input[@*="keyword"]').send_keys('b')#输入关键字b
driver.find_element(By.XPATH,'//input[contains(@*,"word")]').send_keys('c')
sleep(4)
driver.quit()
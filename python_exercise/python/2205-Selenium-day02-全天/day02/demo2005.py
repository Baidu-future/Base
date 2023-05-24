from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()#启动Firefox
driver.get('http://localhost/upload/index.php')#打开ECShop前台首页
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()#点击“登录”
sleep(5)
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/ul/li[1]/font/a[2]/img').click()#点击“注册”
sleep(3)
driver.find_element(By.XPATH,'/html/body/div[4]/form/a').click()#点击“高级搜索“
sleep(3)
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/ul/li[2]/a[1]').click()#点击“查看购物车”
sleep(2)
driver.find_element(By.XPATH,'//*[@id="keyword"]').send_keys('111')
sleep(3)
driver.quit()
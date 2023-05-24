from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/index.php')#打开前台首页
driver.find_element(By.XPATH,"//div[@id='mainNav']/a[last()-2]").click()# 点击“积分商城”
sleep(4)
driver.find_element(By.XPATH,'//a[text()="查看购物车"]').click()#点击“查看购物车”
sleep(4)
driver.find_element(By.XPATH,'//a[contains(@href,"advanced")]').click()#点击“高级搜索”   //a[contains(text(),"高级")]
sleep(3)
driver.find_element(By.XPATH,'//img[contains(@src,"reg")]').click()# 练习：点击“注册”（要求用img的自己的属性值包含xxx进行定位）
sleep(4)
driver.find_element(By.XPATH,'//a[contains(text(),"已有账号")]').click()#点击“我已有账号，我要登录”
sleep(4)
driver.quit()
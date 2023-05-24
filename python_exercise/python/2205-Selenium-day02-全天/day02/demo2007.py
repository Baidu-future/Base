from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("http://localhost/upload/user.php")#打开前台登录页
sleep(2)
# 点击“当前位置：”后的“首页”超级链接
driver.find_element(By.XPATH,"//div[@id='ur_here']/a").click()
sleep(3)
# 点击“积分商城”
driver.find_element(By.XPATH,"//div[@id='mainNav']/a[9]").click()
sleep(3)
# 点击倒序的下拉列表
driver.find_element(By.XPATH,"//select[@name='order']").click()
sleep(3)
# 点击正序的选项
driver.find_element(By.XPATH,"//option[@value='ASC']").click()
sleep(3)
# 点击GO图片
driver.find_element(By.XPATH,"//input[@alt='go']").click()
sleep(3)
driver.quit()
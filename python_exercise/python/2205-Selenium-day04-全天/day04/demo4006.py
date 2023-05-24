from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('http://localhost/upload/user.php')#打开登录页
sleep(3)
driver.find_element(By.LINK_TEXT,'高级搜索').click()#跳转到高级搜索页
sleep(3)
driver.back()#后退，回到上一页，就是登录页
sleep(4)
driver.forward()#前进，转到下一页，就是高级搜索页
sleep(4)
driver.minimize_window()#最小化
sleep(3)
driver.maximize_window()#最大化
sleep(4)
driver.set_window_size(1000,500)
sleep(4)
driver.quit()

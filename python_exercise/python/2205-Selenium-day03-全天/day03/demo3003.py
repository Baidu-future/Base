from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/index.php')#打开前台首页
driver.find_element(By.CSS_SELECTOR,'#ECS_MEMBERZONE > a:nth-child(2) > img:nth-child(1)').click()#点击“登录”
sleep(4)
driver.find_element(By.CSS_SELECTOR,'#keyword').send_keys('a')#输入关键字a
driver.find_element(By.CSS_SELECTOR,'.go').click()#点击搜索
sleep(4)
driver.find_element(By.CSS_SELECTOR,'[href="pick_out.php"]').click()#点击“选购中心”
sleep(3)
driver.find_element(By.CSS_SELECTOR,'form#searchForm>a').click()#点击高级搜索
sleep(3)
driver.find_element(By.CSS_SELECTOR,'#min_price').send_keys('100')# 练习：输入价格最小值100
driver.find_element(By.CSS_SELECTOR,'#max_price').send_keys('999')# 输入价格最大值999
driver.find_element(By.CSS_SELECTOR,'#outstock').click()# 点击“隐藏已脱销的商品”复选框
driver.find_element(By.CSS_SELECTOR,'[value="立即搜索"]').click()# 点击“立即搜索”
sleep(4)
driver.find_element(By.CSS_SELECTOR,'font#ECS_MEMBERZONE>a:last-child>img').click()#点击注册
sleep(4)
driver.quit()
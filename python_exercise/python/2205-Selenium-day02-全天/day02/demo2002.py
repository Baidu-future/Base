from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep #导入time模块里的sleep函数
driver=webdriver.Firefox()#启动浏览器
driver.get('http://localhost/upload/index.php')#打开前台首页
driver.find_element(By.LINK_TEXT,'查看购物车').click()#点击'查看购物车'这个超级链接
sleep(4)#等待4秒
driver.find_element(By.LINK_TEXT,'选购中心').click()#练习：书写一行代码，点击“选购中心”
sleep(5)#等待5秒
driver.find_element(By.LINK_TEXT,'积分商城').click()
sleep(4)
driver.find_element(By.PARTIAL_LINK_TEXT,'总计金额').click()
sleep(4)
driver.find_element(By.PARTIAL_LINK_TEXT,'原装电池').click()# 练习：点击文本里包含“原装电池”的超级链接
sleep(5)
driver.quit()#关闭浏览器，释放资源
from selenium import webdriver
driver=webdriver.Firefox()#启动浏览器
driver.get('http://localhost/upload/index.php')#打开ECShop前台首页
#……
driver.quit()#关闭浏览器
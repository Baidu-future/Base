from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/goods.php?id=24')#打开P806商品详情页
sleep(3)
driver.find_element(By.XPATH,'//img[contains(@src,"bnt_cat")]').click()#点击“加入购物车”
sleep(6)
driver.find_element(By.LINK_TEXT,'删除').click()
sleep(4)
a2=driver.switch_to.alert#切换到消息框
a2.dismiss()#点击“取消”按钮关闭消息框（商品没有被删除）
sleep(4)
driver.find_element(By.LINK_TEXT,'删除').click()
sleep(4)
a3=driver.switch_to.alert#切换到消息框
a3.accept()#点击“确定”按钮关闭消息框（商品被删除）
sleep(4)
driver.quit()

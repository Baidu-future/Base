from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get('http://localhost/upload/goods.php?id=19')#打开三星……商品详情页
sleep(3)
driver.find_element(By.XPATH,'//img[contains(@src,"bnt_cat")]').click()#点击“加入购物车”
sleep(3)
a1=driver.switch_to.alert#切换到消息框
a1.dismiss()#点击“取消”按钮
sleep(3)
#driver.find_element(By.XPATH,'//img[contains(@src,"bnt_cat")]').click()#点击“加入购物车”
sleep(3)
a2=driver.switch_to.alert#切换到消息框
t1=a2.text#获得消息框里的消息文本
print(t1)
a2.accept()#点击“确定”(跳转到登录页)
sleep(3)
driver.quit()
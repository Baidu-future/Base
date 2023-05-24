import schedule
import requests
import smtplib
def job():
    a=requests.get("http://www.baidu.com")
    print(a.text)
schedule.every().day.at("18:42").do(job) # 每天十点半执行

#
while True:
    schedule.run_pending()# 运行所有可运行的任务

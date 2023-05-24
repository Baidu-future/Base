import requests
from requests.cookies import RequestsCookieJar

headers = {
    'Host': 'accounts.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
           }
request_url = "https://accounts.douban.com/passport/login"
res = requests.get(request_url, headers=headers)

status_code = res.status_code
res_header = res.headers
res_cookies = res.cookies
cookie1111 = res.cookies.get_dict()                             # 格式化 字典形式输出
cookie2222 = requests.utils.dict_from_cookiejar(res_cookies)    # 格式化 字典形式输出
for cookie in res_cookies:
    print(cookie.name+"\t"+cookie.value)


print("响应cookies：", res_cookies)


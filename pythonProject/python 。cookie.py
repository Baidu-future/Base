import  Cookie
import  datetime
import   random
expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie["session"] = random.randint(1000000000)
cookie["session"]["domain"] = "baidu.com"
cookie["session"]["path"] = "/"
cookie["session"]["expires"] = \
expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
print "Content-type: text/plain"
print cookie.output()
print "Cookie set with: " + cookie.output()
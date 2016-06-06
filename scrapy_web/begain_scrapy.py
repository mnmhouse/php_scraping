from urllib.request import urlopen
from  urllib.request import   Request
from urllib.parse import  urlencode
from urllib.request import ProxyHandler
import urllib

# response = urlopen("http://www.baidu.com")
# print(response.read())

value = {"username":"pop_1987@126.com","password":"zhanghao8"}
data = urlencode(value)
url = "https://passport.xxx.net/account/login"
request = Request(url,data)
response = urlopen(request)
print(response.read())


#设置代理访问
value = {"username":"pop_1987@126.com","password":"zhanghao8"}
data = urlencode(value)
url = "https://passport.xxx.net/account/login"
request = Request(url,data)

enable_proxy = True
proxy_handler = ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = ProxyHandler({"http" : 'http://some-proxy.com:8080'})
if enable_proxy:
    opener = urllib.request.build_opener(proxy_handler)
else:
    opener = urllib.request.build_opener(null_proxy_handler)

opener.open(request)
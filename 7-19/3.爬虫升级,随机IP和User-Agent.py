import random
from urllib.request import Request ,urlopen ,ProxyHandler ,build_opener


user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
]
headers = {
    'User-Agent':random.choice(user_agent_list)
}
ip_list = [
    '14.155.112.19:9000'
]
# proxies 代理
proxies ={
    'http:': random.choice(ip_list)
}

# 设置爬虫目标 以及 用户标识
request = Request('http://www.baidu.com', headers = headers)
# 创建IP代理对象
proxy_handler = ProxyHandler(proxies)
# urlopen不支持http高级函数，cookie ，验证，代理等内容
# 如果要使用这些内容的话，需要使用bulid_opener对象进行处理
opener = build_opener(proxy_handler)

response = opener.open(request)

print(response.read().decode())

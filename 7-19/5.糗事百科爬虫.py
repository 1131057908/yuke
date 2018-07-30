import re
from urllib.request import Request ,urlopen ,ProxyHandler ,build_opener
import random
base_url = 'https://www.qiushibaike.com/hot/page/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
ip_list = [
    '183.129.207.74	1:4823',
    '58.17.125.215:53281',
    '180.97.193.58:3128',
    '122.72.18.3:80',
    '1.71.188.37:3128',
    '121.42.167.160:3128'
]
proxies = {
    'https:':random.choice(ip_list)
}
def down_load_qiubai_info(pageIndex):
     full_url = base_url + str(pageIndex) + '/'
     request = Request(full_url ,headers = headers)
     response = urlopen(request)
     # 获取对应网页的全部内容
     code = response.read().decode()
     # 正则匹配的内容  从指定的开始为止 到全部内容结束
     # 所以只需要指定开始的位置 不需要指定结束的位置
     #
     # 如果我们想要正则获取某一对标签里面的内容的时候
     # 那么需要将这对标签对写完整 而且在想要获取的内容
     # 上添加() 例如：<h2>(.*?)</h2>
     # pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>',re.S)
     # result = pattern.findall(code)
     # print(result)
     # for name ,age in result :
     #      # 去掉开始和结尾的换行符
     #      name = name.strip('\n')
     #      age = age.strip('\n')
     #      print('作者是',name)
     #      print('年龄是',age)

     pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<a.*?href="(.*?)".*?>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
     result = pattern.findall(code)
     for name , age ,href , content , number , comment in result :
         name = name.strip('\n')
         age = age.strip('\n')
         content = content.strip('\n')
         href = href.strip('\n')
         number = number.strip('\n')
         comment = comment.strip('\n')
         print('作者是',name)
         print('年龄是',age)
         print('详情是',href)
         print('内容是',content)
         print('好笑数',number)
         print('评论数',comment)
         if int(comment) != 0 :
             get_all_comment_with(href)
         else :
             print('该内容暂无评论')

def get_all_comment_with(url):
    detail_url = 'https://www.qiushibaike.com' + url
    print(detail_url)
    proxy_handle = ProxyHandler(proxies)
    request = Request(detail_url ,headers = headers)
    opener = build_opener(proxy_handle)
    response = opener.open(request)
    code = response.read().decode()
    # print(code)
    pattern = re.compile(r'<a.*?class="userlogin".*?title="(.*?)">.*?<span class="body">(.*?)</span>',re.S)
    result = pattern.findall(code)
    print(result)
    print('---------------------------------------------------------------------')

down_load_qiubai_info(1)
"""
座右铭:吃饱不饿，努力学习
@project:7-26
@author:Mr.Huang
@file:json解析2.PY
@ide:PyCharm
@time:2018-07-26 17:47:51
"""

import requests
import json
response=requests.get('http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location=郑州市&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json').text
#现在产生一个字符串response
res_result=json.loads(response)#从字符串转化为python字典
print(type(res_result),res_result)
error=res_result['error']#从字典中通过键取出值
status=res_result['status']
date=res_result['status']
result=res_result['result']
print(result)



cityid=result['cityid']
cityname=result['cityname']
print(cityname,cityid,'00000')
location=result['location']
print(location)
lng=location['lng']
lat=location['lat']

movie=result['movie']
print('movie')
for dex in movie:
    print('dex')
    movie_id=dex['movie_id']
    movie_name=dex['movie_name']
    movie_type=dex['movie_type']
    movie_release_date=dex['movie_release_date']
    movie_nation=dex['movie_nation']
    movie_starring=dex['movie_starring']
    movie_length=dex['movie_length']
    movie_picture=dex['movie_picture']
    movie_score=dex['movie_score']
    movie_director=dex['movie_director']
    movie_tags=dex['movie_tags']
    movie_message=dex['movie_message']
    is_imax=dex['is_imax']
    is_new=dex['is_new']
    movie_big_picture=dex['movie_big_picture']
    movie_wd=dex['movies_wd']
    print(id,movie_name,movie_type,movie_release_date,movie_nation,movie_starring,movie_length,movie_picture,movie_score,movie_director,movie_tags,movie_message,is_imax,is_new,movie_big_picture,movie_wd)
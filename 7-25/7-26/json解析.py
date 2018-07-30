"""
座右铭:吃饱不饿，努力学习
@project:7-26
@author:Mr.Huang
@file:json解析.PY
@ide:PyCharm
@time:2018-07-26 16:20:46
"""
#匹配pip install requests

#第三方用于发送网络请求的一个模块,经常被用于爬虫
import  requests
import json
response=requests.get('http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?').text
print(type(response),response)
res_result=json.loads(response)
print(res_result,type(res_result))
#取error的值
error=res_result['error']
print(error)
#取statu的值
status=res_result['status']
print(status)
#取date的值
date=res_result['date']
print(date)
#取result的值,取出的结果是列表,列表里面包含字典
results=res_result['results']
print(results)
#从result这个列表中取出这个字典
dict_1=results[0]
print(type(dict_1),dict_1)
#cong从dict_1这个字典中通过键取值
currentCity=dict_1['currentCity']
pm_25=dict_1['pm25']
print(pm_25)


#从dict_1字典中取出键index的对应值  值为一个列表
index=dict_1['index']
print(index)

#使用for循环遍历index这个列表

for dex in index:
    #取出来的每一个dex都是字典
    des=dex['des']
    tipt=dex['tipt']
    title=dex['title']
    zs=dex['zs']
    print(des,tipt,title,zs)

weather_data=dict_1['weather_data']
for wea in weather_data:
    date=wea['date']
    dayPictureUrl=wea['dayPictureUrl']
    nightPictureUrl=wea['nightPictureUrl']
    weather=wea['weather']
    wind=wea['wind']
    temperature=wea['temperature']
    print(date,dayPictureUrl,nightPictureUrl,weather,wind,temperature)
"""
座右铭:吃饱不饿，努力学习
@project:7-26
@author:Mr.Huang
@file:json&pickle模块.PY
@ide:PyCharm
@time:2018-07-26 15:42:21
"""
import  json
import  pickle
#json :是采用键值对的结构组成的一组数据,是一种比较轻量的数据交换格式,主要在服务器和前端之间数据传递
#json数据相对于其他格式数据,数据小,传输速度快,解析效率高格式较为统一,解析起来比较方便

#------------------------------------json------------------


dic={"name":'maria','age':'20','is_male':True}
#将字典转化成字符串
#json 布尔值是True False python里面是小写true false
#json.dumps会将字典中所有单引号改编成json中标准的双引号



#--------------------序列化:将python中的对象存储到文件当中----------------------------

# data=json.dumps(dic)
# print(data)
# f=open('test.txt','w',encoding='utf-8')
# f.write(data)
# f.close()

#-----------------------反序列化,将文件中的字符串转化成python对象
f_read=open('test.txt','r',encoding='utf-8')
res=f_read.read()
print(res,type(res))



data2=json.loads(res)
print(type(data2),data2)
print(data2['name'])
print(data2['age'])



#---------------------------------------pickle-******************

#pickle与json一样(基本上使用json足够)
#pickle与json区别
# json只能处理基本的数据类型,pickle能处理所有python数据类型
#2. json用于各种语言之间字符转换,pickle只能用于python的序列化或者python程序之间的对象的网络传输

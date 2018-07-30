"""
座右铭:吃饱不饿，努力学习
@project:7-26
@author:Mr.Huang
@file:time 模块.PY
@ide:PyCharm
@time:2018-07-26 10:52:58
"""

import time

# 1-获取时间戳,时间戳是以单位为秒 从1970年1月1日00:00到现在经历多少秒
# 时间戳一般用于验证登录是否过期
# timetamp=time.time()
# print(timetamp)
# #2.localtime():获取本地时间的函数,返回值是元组
# localtime=time.localtime()
# print(localtime)
# print(localtime.tm_year,localtime.tm_mon,localtime.tm_mday)


# 3.asctime():获取格式化的本地时间
# local_time=time.asctime(time.localtime())
# print(local_time)
# 4.将本地时间元组格式化成2018-7-26的  11:01:xx的形式
# strfrtime():将时间元组转化为时间字符串
# time_1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
# print(time_1)
# strptime将格式化的字符串转化时间元组
string = 'Thu jul 26 14:04 2018'
time_2 = time.strptime(string, '%a %b %d %H:%M %Y')
print(time_2)

string1 = '2018-07-26 14:20:55'
time_3 = time.strptime(string1, '%Y-%m-%d %H:%M:%S')
print(time_3)


#2018-7-26  14:04 Thu Jul
string2='2018-7-26  14:04 Thu Jul'
time_4=time.strptime(string2,'%Y-%m-%d %H:%M %a %b')
print(time_4)




#将时间元组转换成格式化字符串:14:05:30 7-26-18
time_5=time.strftime('%H:%M:%S %m-%d%-%y',time.localtime())
print(time_5)



#**********************************
#1-获取本地时间

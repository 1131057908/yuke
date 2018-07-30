"""
座右铭:吃饱不饿，努力学习
@project:7-26
@author:Mr.Huang
@file:datatime.PY
@ide:PyCharm
@time:2018-07-26 14:35:35
"""
import datetime


#1.获取当前时间和日期
datetime_dt=datetime.datetime.today()
print('当前时间和日期是:{}'.format(datetime_dt))

#2.格式化时间和日期
datetime_str=datetime_dt.strftime('%Y-%m-%d %H:%M:S')
print('当前时间和日期格式化之后为{}'.format(datetime_str))

#3.设置时间间隔

time_delta=datetime.timedelta(hours=3)
print('当前时间间隔为{}'.format(time_delta))



#把时间往后延迟三个小时
datetime_pre=datetime.datetime.today()+time_delta
print('时间延后三小时:{}'.format(datetime_pre))

#获取当前时间
time=datetime.datetime.today().time()
print('当前时间为{}'.format(time))


#6.将时间和日期转化成时间戳
time_s=datetime.datetime.today().timestamp()
print('现在的时间戳为{}'.format(time_s))




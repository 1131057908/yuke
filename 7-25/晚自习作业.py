"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:晚自习作业.PY
@ide:PyCharm
@time:2018-07-25 19:34:20
"""
# 1.利用map()和reduce()函数，实现类似于int()的功能。比如:'123'-123
# 2.利用map()实现类似于字符串的lower()函数的功能。比如将AbCdEF全部转换成小写
# from functools import reduce
# result1=map(int,['12312'])
# print(result1)
# for x in result1:
#    print(x,type(x))

def is_lower(str1):
    for s in str1:
        if s.isupper():
            return s.lower()
        else:
           return s
res=map(is_lower,'aBcD')
for s in res:
    print(s,end='')








"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:reduce函数.PY
@ide:PyCharm
@time:2018-07-25 10:00:43
"""

from functools import  reduce
#reduce()接受两个参数 "第一参数:函数,第二参数:序列
#作用;将序列中前两个元素运算,然后在和第三个元素运算,一次往下执行
def  add(x,y):
    res=x+y
    return res
result=reduce(add,['a','b','c','d'])
print(result)
#第一次运算a+b 结果ab
# 第二次运算ab+c 结果abc


result1=reduce(add,[1,2,3,4])
print(result1)
#使用lambda改造
result2=reduce(lambda x,y:x+y,[1,2,3,4])
print(result2)
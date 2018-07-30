"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:main.PY
@ide:PyCharm
@time:2018-07-25 16:41:07
"""
#import 本质:相当于先把my_module这个模块先解释执行一遍,然后赋值给My_module这个变量
#最后通过这个变量调用my_module里面的name say_hello()
import my_module

# print(my_module.name)
# my_module.say_hello()
#from ....import.....本质是吧my_module里面的aage,say_haha先放在main文件执行一遍,所以就可以直接使用

from my_module import age,say_hello
# print(age)
#
# print(age)
# say_hello()
# from my_module import *
# from my_module import  say_hello as say_haha_one
# say_haha()
# say_hello()

#当被导入模块中存在__all__=[]则使用from 模块名 import *这种方式进行导入,只能导入__all__[]
# 里面的内容
# from my_module import *
# say_hello()
# print(name)
# print(age)








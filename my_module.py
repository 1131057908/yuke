"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:my_module.PY
@ide:PyCharm
@time:2018-07-25 16:40:29
"""


__all__=['say_hello','name']
name='张三'
age=110
def say_hello():
    print('hello!')
def say_haha():
    print('haha')
print('my_module里面执行了')
if __name__=='__main__':
    say_haha()



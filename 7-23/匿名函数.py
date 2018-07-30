"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:匿名函数.PY
@ide:PyCharm
@time:2018-07-23 20:48:12
"""
#lambda(匿名函数的关键字，)：python中lambda创建匿名函数，不能给函数设置函数名，和普通函数相比lambda相当于生成一个表达式，lambda语法简单可以封装一些简单的逻辑

#为甚使用匿名函数：
#1 不需要定义函数名，节省内存变量的定义空间
#2.可以使代码更加简洁



#正常的使用函数来定义一个数字相加
#
# def add(x,y):
#     return  x+y

# res=add(10,20)
# print(res)
# #使用lambda来改造数字相加的函数
# #x,y 相当于普通哈数的参数，：分隔符，x+y相当于返回值
# res_lambda=lambda x,y:x+y
# #通过res_lambda这个变量来执行lambda函数
# res1=res_lambda(10,20)
# print(res1)
#
#
# #不添加参数的lambde函数
# res2=lambda :print('这是一个没有参数的函数')
# print(res2)
# lambda 形参:条件,序列


# def hu():
#     print('这是一个没有参数的函数')
# hu()


#lambda加上条件判断
# def bijiao(x,y):
#     if x>y:
#         print('x>y')
#     else:
#         print('y>x')
# bijiao(2,3)

# res=lambda  形参:print() 判断条件
#传递参数  res(实参)
res3=lambda x,y:print('x>y')if x>y  else print('y>x')
res3(2,3)

# #跟lambda函数设置默认参数
def panduan(name='张三'):
    if name=='张三':
        print('三门')
    else:
        print('不是')
panduan()
res5=lambda name='张三':print('asan')if name=='张三'else print('不是')
res5(name='李四')

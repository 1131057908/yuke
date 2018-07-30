"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:类的声明.PY
@ide:PyCharm
@time:2018-07-30 10:52:46
"""


class People(object):

    #__init__:这个初始化函数,会在对象被创建的时候,自动执行函数的调用,不需要手动打点调用
    #__init_在类中不是必须要定义的,但当声明属性的时候,必须通过__init__函数调用
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        print('我是在对象被创建的时候自动调用')
        #类中定义的函数;第一个参数,必须是self,self相当于一个形参.但是它是由解释器自动传值,self后面可以定义我们需要的参数
    def eat(self):
        print('吃撒')
    def sleep(self):
        print('睡觉')
    def work(self):
        print('工作')
#创建一个对象,p1,自动执行了对象的初始化函数,__init__并且给初始化函数传递了参数,传递参数的时候,参数实际上隐含了一个实参,这个实参会赋值给__init__()函数的self形参
p1=People('p1',20,'男')
#当对象操作类中属性的时候,对象名.属性名///操作类中函数的时候,对象名.函数名()
print(p1.name,p1.sex,p1.age)
p1.work()


#关于对象创建过程(对象内存)
#每次通过People类创建对象的时候,python解释器都会给对象分配给一个单独的内存空间,会将People类中定义的属性复制一份,存放到对象内存中,同时内存具有一定的特征,创建出来的每一个对象都是唯一的,独立的,不允许重复

#@虽然所有People类的对象都是复制了name,age,sex,这些属性,但是复制出来的每一个属性都是存在么一个对象各自的内存中,每个对象都互不相干
p2=People('p2',20,'男')
print(id(p1),id(p2))
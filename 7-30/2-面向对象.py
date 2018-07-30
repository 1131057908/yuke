"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:面向对象.PY
@ide:PyCharm
@time:2018-07-30 09:55:23
"""
#类和对象的基本定义:
#类;具有相同属性或行为的事物通常为类
#对象




#类和对象的关系:对象是类的实例,类是对象的模板
#区分类和对象
#1-车(类),王的二手奥拓(对象)
#2-狗(_类)曹的藏獒(对象)
#水果(类):于啃得榴莲(对象)



#面向对象编程中的类和对象:类在面向对象过程中,是一种抽象化的概念,类不会占据内存空间,类只要为了辅助创建对象而存在,对象才是面向对象编程的核心,一般来说,所有函数的执行还有变量的调用必须通过对象才能完成,对象在内存中是实际存在的,会消耗内存空间,对象也称为实例化对象


#面向过程中的类的作用:通常情况下,会在类中指定一些属性和行为,当时用实例化对象的时候,那么对象就用于类中指定的属性和行为


#类是由于每一个对象共同抽象化出来的概念,至于类中指定那些属性和行为,
# 是由对象决定的,因为具体操作这些都是对象来执行


#面向对象编程的时候,首先考虑如何设计一个类,类中的属性和行为是对象需要的属性和行为为类决定的

#假如想声明一个人类:

#人类需要的属性:性别,年龄,姓名

#人类需要的行为:吃饭,睡觉,工作(行为:函数)

#class:声明类的关键字
#people:自定义的类名,遵循大驼峰命名
#object:表示当前类People的父类,也称为基类或者根类,表示一种继承关系
class People(object):




    # __init__:对象初始化函数,该函数就是指定对象属性
    # 3name/age/sex叫做init'函数的形参,等待实参传值'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('吃撒')
    def sleep(self):
        print('睡觉')
    def work(self):
        print('工作')
#类声明完了,可以根据类来创建对象
# 创建对象zhangsan 将值传入
zhangsan=People('张三',20,'男')
print(zhangsan.name,zhangsan.sex,zhangsan.age)
zhangsan.eat()
zhangsan.sleep()
zhangsan.work()

#创建lisi对象
lisi=People('李四',20,'女')
print(lisi.name,lisi.age,lisi.sex)
lisi.work()
lisi.sleep()
lisi.eat()
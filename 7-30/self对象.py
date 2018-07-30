"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:self对象.PY
@ide:PyCharm
@time:2018-07-30 14:04:43
"""
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('self=',self)
    def show(self):
        print('调用show函数','self=',self)



#self 本身指代的就是一个对象,这个对象是student类类型,self具体指代是student哪一个对象,是由student中那一个对象在使用属性或者函数(方法)来决定的.
stu=Student('张三',20)
stu.show()

stu_1=Student('李四',22)
stu_1.show()


#对象的内存具有唯一性,两个不同对象内存不一样

#stu和student(''张三',20)之间的关系

#第一步:当student('张三',20)执行完毕,实际上已经实例化出来了一个对象,与此同时对象在内存中已经产生
#第二步:将内存已经产生的这个对象赋值给stu这个变量(指针),是这个变量(指针)来代替student('张三',20)这个对象来执行函数的调用,属性的调用
#指针是用于指向一个对象的内存地址,方便去操作对象,管理对象
#一个对象的内存地址可以有多个指针指向,但是一个指针只可以指向一个对象的内存地址


class People(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def run(self):
        print('运动')
xiaoxiao=People('小小',20,'女')
xiaoxiao.run()
print(xiaoxiao.age,xiaoxiao.name,xiaoxiao.sex)
"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:文件的操作.PY
@ide:PyCharm
@time:2018-07-30 11:21:47
"""

class People(object):
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

p1=People('p1',20,'男')
p2=People('p2',30,'女')
#动态给某一个对象添加属性
p1.weight=100
print(p1.weight)

#hasttr()判断某个对象是否含有某个属性,
#hasttr(对象名,属性名)该函数返回布尔值
if hasattr(p2,'weight'):
    print(p2.weight)
else:
    print('没有这个属性')
#getattr():用于获取某一个对象的属性值
#getattr(对象名,属性名,属性默认值):当获取属性存在,则直接获取属性值,不存在则返回默认值,防止报错
print(getattr(p1,'name','100'))
print(getattr(p2,'height','200'))
# setattr():用于给某一个对象添加属性
# setattr(对象名,属性名,默认值):当添加的属性不存在,的时候,则会给该对象添加一个属性,如果已经存在,则会修改该对象的属性值
setattr(p2,'color','black')
print(p2.color)
setattr(p2,'age','50')
print(p2.age)

#delattr(对象名,'属性名'):删除某一个对象的属性
delattr(p2,'color')
try:
    print(p2.color)
except  Exception as  e:
    print('错误信息:',e)
"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:类变量和实例变量.PY
@ide:PyCharm
@time:2018-07-30 15:47:33
"""
#类变量:只有类名才能调用的变量,类变量一般在函数体之外
#实例变量:



class Employee(object):
    #声明一个类变量,记录员工总人数
    total_Emplyee_number=0#类变量需要打点调用

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        #类变量在各个对象
        Employee.total_Emplyee_number+=1

    def get_total_number(self):
        print('员工总体人数:',Employee.total_Emplyee_number)
        #类变量在各个对象间共享,类只初始化一次
e1=Employee('张三',6000)
e1.get_total_number()
#实例变量的调用:对象名,实例变量
e2=Employee('李四',8000)
e2.get_total_number()



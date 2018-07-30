#Author;黄
#必备参数:实参,形参数量上必须保持一致
def sum (a,b):
    c=a+b
    print(c)
sum(1,2)
#命名关键字,通过定义关键子获取实参的值,与形参顺序无关
def show (name,age):
    print('姓名是:%s-年龄是%s'%(name,age))
show(age=20,name='张三')
# 默认参数  有了默认参数,不用填信息,如果填写信息
# 使用默认参数的时候,如果给形参传递了实参,则形参会接受实参的值
# 如果没有这个形式传递实参,则形参会采用默认值
# 一般可用于密码账号登陆的时候  或者数据库连接的时候
def show1(name='',password='123456'):
    print('账号是%s'%name)
    print('密码是%s'%password)
show1()
show1('Uzi','678910')
# 位置参数形参的数量会根据实参的数量变化而变化
#*args :接受n个位置参数,并把位置参数转换成元组形式
def show2(*args):
    print(type(args))
    print(args)
show2(1)
show2(1,2)
show2(1,2,3)

#**kwargs:关键字参数
#kwargs 把n个关键字参数转换成字典的方式

def show3(**kwargs):
    print(type(kwargs))
    print(kwargs)
show3(name='zhang',age=8,sex='male')


# 写一个函数,把以上所有参数全部添加进去
def show4(name,*args,age=20,**kwargs):
    print('----------',name)
    print(args)
    print(age)
    print(kwargs)
show4(10,20,'zhang','sun',age=42,sex='male',father='马云')
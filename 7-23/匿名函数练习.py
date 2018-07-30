"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:匿名函数练习.PY
@ide:PyCharm
@time:2018-07-24 20:16:57
"""
#正常使用函数相加
def add(x,y):
    return x+y
res=add(10,20)
print(res)


res_lan=lambda x,y:x+y
res1=res_lan(10,20)
print(res1)



res3=lambda :print('这是无参函数')
print(res3)


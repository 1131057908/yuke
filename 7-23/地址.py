"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:地址.PY
@ide:PyCharm
@time:2018-07-23 22:47:19
"""
list1=[1,2,3]
list2=[1,4,2]
# 2被当成一个整数对象分别实例化到list1[1]和list2[1]中,他们两个列表中的2是同一个东西
print('2',id(2))
if id(list1[1])==id(list2[1]):
    print('2',id(list1[1]))
    print(True)
else:
    print(False)
print('地址是%s'%id(list1[1]))
print('地址是%s'%id(list2[2]))




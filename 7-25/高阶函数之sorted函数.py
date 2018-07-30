"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-25
@author:Mr.Zhang
@file:高阶函数之sorted函数.PY
@ide:PyCharm
@time:2018-07-25 10:51:28
"""
#sorted():用于对个序列进行升序排列。第一个参数:序列，第二个参数key:用于指定一个只接收一个参数的函数，这个函数用于从序列中的每个元素中提取一个用于排序的关键字，默认值为None。第三个参数reverse:有两个值，一个为True，一个为False。如果reverse=True，则列表中的元素会被倒序排列。

#sorted默认按照ASCLL排序
from functools import cmp_to_key
#
# list1=[30,50,70,3,9]
# list2=sorted(list1)
# print('排列之后的结果',list2)


#5,3,2,4,1
#1,2,3,4,5
#5,4,3,2,1

#a:97,b:98,c:99,d,100
# list4=['b','c','a','d']
# list3=sorted(list4,reverse=True)
# print(list4)
# print('倒序排列：',list3)
# #
# list5=[('b',4),('a',0),('c',2),('d',3)]
# list6=sorted(list5,key=lambda x:x[0])
# print('=====',list6)

# #如果使用sorted()函数实现对一个序列的降序排序。

list7=[20,15,70,3,9]
# list8=sorted(list7)
# print('升序排列:',list8)
# #
# #如果x>y返回-1，x<y返回1，是按照降序排列的
# #如果x>y返回1，x<y返回-1，则就是默认的升序排列
def revsersed(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

result=sorted(list7,key=cmp_to_key(revsersed))
print('降序排列：',result)

#
# #面试中的常考题：sort和sorted的区别
# #sort排序会改变原来的list，而sorted排序只是对原有列表进行排序返回了一个新的经过排序之后的列表，并不会对原有列表进行改动。
# #sorted用于对一个序列进行排序。而sort只能用于列表的排序。
# #sort只是单纯的对列表进行内部排序，并没有返回值。
#
# print('*****************')
# list9=[9,5,3,8,7,1]
# print(list9)
# list9.sort()
# print(list9)
#
#
# print('****************')
# list10=[11,15,9,7,6]
# print(list10)
# print(sorted(list10))
# print(list10)
#
# test=(1,2,5,9,8)
# # test.sort()
# print(sorted(test))
#
#
#

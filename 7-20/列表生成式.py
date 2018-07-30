"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:列表生成式.PY
@ide:PyCharm
@time:2018-07-20 15:41:42
"""

#列表生成式;快速 生成列表的一种方式
my_list=[]
for x in range (1,11):
    res=x**2
    my_list.append(res)
print(my_list)


Fast_list=[x**2 for x in range (1,11)]
print(Fast_list)
#加入if判断
Fast_list_1=[x**x for x in range (1,11) if x!=2]
print(Fast_list_1)


#遍历1-11之间数字当数字为奇数结果进行平方运算
fast_list_2=[x**2 for x in range (1,11) if x%2==1]
print(fast_list_2)


#双重for循环
fast_list_3=[x*y for x in range(1,4)  for y in range(1,4)]
print(fast_list_3)


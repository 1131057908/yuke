"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:面试经常遇到的大坑.PY
@ide:PyCharm
@time:2018-07-23 20:20:19
"""
def keng(i,result=[]):
#id()显示对象内存地址
#一个对象对应的内存是唯一的
    print('未添加对象前的列表的内存地址：%s'%id(result))
    for x in range(i):
        result.append(x*x)
    print(';添加完数据之后的列表的内存地址：%s'%id(result))
    return result


res=keng(3)
print(res)
res1=keng(3)
print(res1)
res2=keng(3,[1,2,3])
print(res2)
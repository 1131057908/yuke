"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:生成器函数练习.PY
@ide:PyCharm
@time:2018-07-24 20:35:08
"""
def test():
    list1=[]
    for x in range(1,10):
        list1.append(x)
    return list1
res=test()
print(res)

def test_1():
    for x in range (1,10):
        yield x
generator=test_1()
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
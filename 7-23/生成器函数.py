"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:生成器函数.PY
@ide:PyCharm
@time:2018-07-23 22:06:54
"""
#生成器函数：当一个函数带有yield关键字的时候，那么它将不是一个普通函数，而是一个生成器generator
#yield 和 return ;这两个关键字十分相似，yield每次只返回一个值，二return则会把最终的结果一次性返回
#每当代码执行到yield的时候就会直接将yield后面的值返回去，下一次迭代的时候，会从上一次遇到yield之后的代码开始运行
def test():
    list1=[]
    for x in range (1,10):
        list1.append(x)
    return  list1
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
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator))

#生成器函数的例子：母鸡下蛋
#1.一次性把所有的鸡蛋全部下下来。
#如果一次性把所有的鸡蛋全部下下来，一是十分的占地方，二鸡蛋容易坏掉。
# def chicken_lay_eggs():
#     #鸡蛋筐列表
#     basket=[]
#     #母鸡下蛋
#     for egg in range(1,101):
#         basket.append(egg)
#     return basket
# eggs=chicken_lay_eggs()
# print('一筐子鸡蛋：',eggs)
#
# #这样做的好处：第一是省地方，第二，下一个吃一个，不会让鸡蛋坏掉。
# def chicken_lay_eggs_1():
#     for egg in range(1,101):
#         print('战斗母鸡正在下第{}个蛋'.format(egg))
#         yield egg
#         print('我给{}蛋给吃了！'.format(egg))
# eggs_1=chicken_lay_eggs_1()
# print(next(eggs_1))
# print(next(eggs_1))
# print(next(eggs_1))
#
#

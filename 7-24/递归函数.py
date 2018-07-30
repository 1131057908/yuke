"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-24
@author:Mr.Zhang
@file:递归函数.PY
@ide:PyCharm
@time:2018-07-24 17:16:35
"""
#递归函数的定义:如果一个函数在内部调用自身本身，那么这个函数就叫做递归函数。
#递归函数的调用：
#1.递归函数必须有一个明确的结束条件(有一个函数的出口)
#2.递归函数每次进入更深一层递归的时候，问题规模相比上次递归都应有所减少。
#3.递归效率不高，递归层次过多会导致栈溢出。(在计算机当中，函数的调用是通过栈这种数据结构实现的，每当进入一个函数的调用，栈就会加一层栈帧，每当函数返回。栈就会减少一层栈帧，栈的大小不是无限的。)


#栈溢出:栈溢出也是缓存区溢出的一种。程序的运行的时候，为了临时存储数据的需要，一般都要分配一些内存空间。通常分配的这些空间被称之为缓冲区，如果向缓冲区写入其超过自身长度的数据，会导致缓冲区无法容纳，就会造成缓存区以外的存储单元被改写。这种现象就叫做缓冲区溢出。

#阶乘:5!=5*4*3*2*1
#通过一个循环来实现阶乘
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *=i
    #for i in range(2,6):
    #i：2,3,4,5
    #result * = 2  相当于 result=result*2 相当于result=1*2
    #result *= 3   相当于result = result*3 相当于 result = 1*2*3
    #result *=4     相当于result = result * 4 相当于result = 1*2*3*4
    #result *=5     相当于result = result * 5  相当于 result = 1*2*3*4*5
    return result
res = factorial(5)
print('阶乘的结果:',res)

#通过递归函数来实现阶乘
def factorial_1(n):
    if n==1:
        return n
    else:
        return n*factorial_1(n-1)

res1=factorial_1(5)
print('阶乘的结果:',res1)

# res2=factorial_1(999)
# print('阶乘的结果：',res2)
'''
factorial_1(5)
5 * factorial_1(4)
5*4*factorial_1(3)
5*4*3*factorial_1(2)
5*4*3*2*factorial_1(1)
5*4*3*2*1
'''

#如果一个递归函数不设置结束条件，默认最大的递归次数是999次。(如果不设置最大递归次数会出现死循环，给机器搞崩溃了，所以设置一个保护机制让最大的递归次数为999次。)
#这种情况相当于面临着一个死循环
# def calc(n):
#     return calc(n)
# calc(999)


#尾递归：（解决递归调用的时候栈溢出的一种方法）
#尾递归的定义:在函数的时候，调用自身本身，并且return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归优化，尾递归函数的特点就是在回归的过程中不做任何操作，这样就可以使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
#尾递归的原理:当编译器检测一个函数调用是尾递归的时候，它就覆盖当前的活动记录而不是去栈中创建一个新的。编译器可以做到这一点，因为递归调用是当前活跃期内最后一条待执行的语句，于是当这个调用返回时栈帧并没有其他可做事情，因为也就没有保存栈帧的必要了。通过覆盖当前的栈帧而不是在其之上重新添加一个。这样所使用的栈空间就大大缩小了，这使得实际的运行效率会更高。

def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)

res3=fact(999)
print(res3)

#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#针对尾递归优化的语言可以通过尾递归防止栈溢出，尾递归事实上和循环是等价的。没有循环语句的编程语言只能通过尾递归实现循环。
#python标准的解释器没有针对尾递归做优化，任何递归函数都会出现栈溢出的情况。

"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:·函数讲解.PY
@ide:PyCharm
@time:2018-07-23 19:13:18
"""




#函数：为什么使用函数？因为没有函数的编程只是在单纯的写逻辑代码，只能够copyy一份但是使用函数可以提高代码重复使用效率，提升开发效率
#第一步：声明一个函数，在函数里面写逻辑代码
#第二步：调用函数，执行编写的逻辑代码

print('今天是周一')
print('今天是周二')
print('今天 是周三')

#怎么声明一个函数，在函数里面写逻辑代码
#调用函数，执行编写的逻辑代码

#def 声明函数，的关键字，shuchu（）函数可以自定义，（）用于定义函数的参数，如果没有内容就表示该函数没有参数：下面的东西，要封装的代码逻



#声明一个无返回值，无参数的函数
def shuchu ():
     print('今天是周一')
     print('今天是周二')
     print('今天是周三')
# 调用函数，函数名+括号
shuchu()
shuchu()
shuchu()


#2.声明一个有返回值无参数的函数


#一个函数为什么要有返回值，因为一个函数最终的执行结果，后面的程序才能根据这个执行结果进行其他操作
# def huang():
#     c=int(input('qingshuru :'))
#     d=int(input('请输入：'))
#     e=c*d
#     return  e
# res=huang()
# print(res)
# f=res*10
# print(f)


#3.声明一个无返回值，有参数的函数
#a，b 形参

def chufa(a,b):
    c=a/b
    print(c)
    # return c
#20,10为实际参数，实参是给a，b这两个形参赋值  a=10，b=2.5
chufa(20,10)

#有返回值有参数的函数
def jian(a,b):
    c=a-b
    return c
res=jian(8,5)
print(res)
res1=res+10
print(res1)
#return关键字作用
#1用于返回函数的执行结果
#2. 用于结束当前代码的执行，使用return关键字结束代码执行的时候，return必须位于函数内部，区别于break
def test():
    for x in range (1,11):
        if x%4==0:
            return
        else:
          print('============',x)
test()


def func2():
    for i in range(1,11):
        if i %2==0:
            break
        #到第一个符合条件的情况截至。不输出符合条件的语句，并停止
        print(i)
func2()
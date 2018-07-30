# 为什么使用函数?因为没有函数的编程,只是单纯的写逻辑,如果想重用逻辑,唯一的办法
# 就是copy一份源代码,但是使用函数就可以将逻辑相同的代码封装这样既可以提高代码逻辑的
# 重复使用率,在函数里面写逻辑代码
# 声明函数,在函数里编写逻辑代码
# 调用函数,执行编写的逻辑代码
#
# 声明函数,def声明函数的关键字Add是自定义函数的名称,()用于定义函数的参数
# 如果没有内容就表示该函数没有参数
# 无返回值,无参数

def add():
    b=2
    a = 1
    c=a+b
    print(c)

# 调用函数
add()

#有返回值,无参数的函数,一个函数为什么要返回值,因为想要一个函数的最终执行结果,后面的程序才可以根据致个执行结果进行其他caoz操作
# return;是返回函数结果的关键字

def cheng():
    c=10
    d=20
    e=c*d
    return e
res=cheng()
print(res)
f=res*10


# 无返回值,有参数的函数
# a.b称之为形参
def chu(a,b):
    c=a/b
    print(c)
# 10  2.5 称之为实参  形参用于接受形参的值,形参给形参赋值
chu(10,2.5)
chu(20,4)


# 有返回值  有参数


def jian(a,b):
    c=a-b
    return c,b,a
res=jian(10,5)
print(res,type(res))

# res1,res2,res3=jian(10,5)
# print(res1,res2,res3)
#return  关键字作用
# 用于返回函数的结果
# 用于结束当前代码的执行 视同return 关键字运行的时候 必须位于函数的内部
def test():
  for x in range(1,11):
    if x==5:
      return  x
  else:
   print(x)
test()
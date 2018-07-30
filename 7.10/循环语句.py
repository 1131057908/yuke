# 循环打印1-10的数字
# while 循环
# ____________
# x 是一个变量,可以自定义
# range()python的你内置函数,用于设置范围range()函数取头不取尾
# range(1,11)取值到1-10,range(1,12)取值到1-11
for x in range(1,11):
    print(x)
string='恭喜lpl获得洲际赛冠军'
for s in string:
    print(s)
 # \一般能使用for循环遍历的,都可以称为可迭代对象.
 # 循环中的两个关键字:
# continue:用于中断for/whle循环中的某一次循环,剩下的循环还会执行完毕
# break:用于中断整个for/while循环
for y in range(1,6) :
    if y==2:
        break
    else:
     print(y)
for y in range (1,6):
    if y==2:
        continue
    else:
     print(y)
# --------------while----------
# while 循环,执行的依据是判断while后面的条件是否成立,一般用于不知道循环次数的情况下
#     使用while]循环
# 当while后面跟的条件一直为真就会成为死循环
# while True:
num=1
#     print('这是一个死循环')
while  num<=520:
    print(num,'我爱你')
    num+=1

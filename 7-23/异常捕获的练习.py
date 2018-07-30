"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:异常捕获的练习.PY
@ide:PyCharm
@time:2018-07-24 08:54:21
"""
#模板:
# try:
#    # 捕获异常的代码
# except Exception as e:#捕获异常原因并传递给e
#
# else:
#
#
#
#
# try:
#     #写要捕获的异常代码
#     pass
# except Exception as e:
#     # Exceeption :异常类，基本上能捕获常见的异常的情况，表示异常原因
# # e 用于接受错误的原因
#     pass
#     # 出现异常时，需要设置的代码逻辑
#     #当try 代码执行成功的时候，则不会执行except Exception as e里面的代码
# else :
#     pass
# #如果try里面的代码执行成功，则紧接著会执行else中代码,try不成功执行则不会执行else里面代码
# finally:
#     pass
#  #不管try执行成功还是失败，最终都会执行finally语句里面的代码
#  # example
# list1=[1]
# print(list1[0])
# try:
#     print(list1[0])
# except Exception as e :
#     print('try里面的代码没有执行成功，则会执行我')
# else:
#     print('try里面代码执行成功，则会执行我')
# finally:
#     print('无论怎样我都执行')
# #能输出错误原因
# try:
#      print(list1[1])
# except IndexError as e:
#     print('try里面的代码出现异常没有执行成功，所以需要执行我！')
#     print('错误的原因error:',e)
# else:
#     print('try里面的代码执行成功，则会接着执行我！try里面的代码没有执行成功，则不会执行我！')
# finally:
#     print('不管try执行成功还是失败，都最终会执行我！')

#在函数内部自定义一个一个异常：当调用该函数的时候，如果不符合函数内部定义的条件，
# raise ：抛出异常原因的关键字
def is_outrange(age):
    if age<16:
        raise Exception('小于16岁，不能谈恋爱')
    else:
        return True

res=is_outrange(18)
try:
    res=is_outrange(18)
except Exception as e:
    print('错误原因error：',e)

#面试常见问题
# IndexError:索引错误
# ImportError:导入错误
# NameError:尝试访问一个没有声明的变量
# SyntaxError:语法错误
# AttributeError:尝试访问位置的对象的属性
# KeyError:请求一个不存在的字典关键字
# ValueError:传给函数的参数类型不正确







"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:异常捕获练习.PY
@ide:PyCharm
@time:2018-07-24 19:43:28
"""
#raise:抛出异常原因关键字


def is_outrange(age):
        if age<16:
                raise  Exception('小于16周岁不能谈恋爱')
        else:
            # return True
              yield
res=is_outrange(15)
print(res)
try:
    res=is_outrange(15)
except Exception as e:
    print('错误原因error:',e)
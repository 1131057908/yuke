"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:利用map.reduce实现int.PY
@ide:PyCharm
@time:2018-07-27 09:26:17
"""
#字符串'123'转换成整数123
#两个步骤
#第一步:现将字符串'1','2','3'的每一个字符转换为数字
#第二步:再讲每一个数字进行相应处理,使其成为整数123
from functools import reduce
def char_to_number(string):
    all_number_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    #以参数string为键取出all_number_dict里面的值
    return all_number_dict[string]
res = list(map(char_to_number, '123'))
print(res)

def result_number(x,y):
    res=x*10+y
    return res
result=reduce(result_number,res)
print('最终结果:',result,'最终类型',type(result))


#整体封装,使其使用起来和int函数一样方便
def INT(s):

   def char_to_number(string):
    all_number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    # 以参数string为键取出all_number_dict里面的值
    return all_number_dict[string]

   def result_number(x, y):
       res = x * 10 + y
       return res

   return  reduce(result_number, map(char_to_number,s))
res=INT('456')
print(type(res))
print(res)


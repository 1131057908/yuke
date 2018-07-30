"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:列表生成器.PY
@ide:PyCharm
@time:2018-07-20 15:54:33
"""
#列表生成器

fast_list=(x*x for x in range (1,3))
print(fast_list)
#使用next一次从生成器中取出一个值，如果元素取完后再去会报错
print(next(fast_list))
for x in fast_list:
    print(x)
#列表生成器与列表生成式区别  kuohao
# fast_list_1=[x*x  for x in range(1,100)]
# print(fast_list_1)


fast_list_2=(x*x for x in range(1,1000000))
print(fast_list_2)
#通过列表生成式  会依次将所有的值计算出来，存放在列表中，但是由于计算机内存限制，列表的容量也有限，如果一个数据列表庞大，但是只需访问前几个元素，那么就会导致其他元素占用的内存浪费
#通过列表生成器 并不会一次性将所有计算结果存入列表，而是使用某一值得时候，才会去动态计算结果并返回，未使用的值不计算


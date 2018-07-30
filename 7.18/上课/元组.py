#创建一个元组
tuple1=('张三',20,6.55,True)


print(type(tuple1),tuple1)

#创建一个只有一个元素的 元组
tuple2=(1,)
print(type(tuple1),tuple1)
#创建一个空元素
tuple3=()





#---------------------------查询元素------------
# a=tuple1[0]
# print(a)
# b=tuple[1]
# print(b)
#切片查询与列表相同
#列表切片查询是列表  元组切片查询是元组
# c=tuple[0:3]
# print(c)

#通过索引遍历一个元组

for x in range (0,len(tuple1)):
    print(x+1,tuple1[x])

#直接遍历元组中、的元素

for y in tuple1:
    print(y)
#通过枚举函数遍历
for  index, value in enumerate(tuple1):
    print(index,value)
#---------------修改和删除元素----------
tuple4=['张三','李四','[(40,50)]','20']
# tuple4.pop[2][0]
# print(tuple4)0
#-------------常用函数-------
#3count()
tuple5=(20,20,20)
res7=tuple5.count(20)
print(res7)

#index()返回元素索引值
res8=tuple5.index(20)
print(res8)

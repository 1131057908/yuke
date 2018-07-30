# 元组与列表一样是容器类型的数据,元组只能在创建的时候添加数据,创建完成之后可以查询数据,但是元组的一级元素不可被删除和更改,一般在创建元组的时候在最后一个元素后面加上逗号
# 创建一个yuanzu
tuplel=(20,9.11,'亚洲捆绑',True,)
# ---------------------------查询数据----------------------------
a=tuplel[0]
print(a)
b=tuplel[1]
print(b)
# 切片查询
c=tuplel[0:3]
print(c)
# 元组切片查询,返回的是一个元组
# 列表查询,返回的是一个列表
for x in range(0,len(tuplel)):
     print(x)
# 直接通过索引进行遍历
for y in tuplel:
    print(y)
# 通过枚举查询
for index , value in enumerate(tuplel):
    print(index,value)
# 一级元素不能被修改 ,二级元素可以
tuple2=(20,30,'meiko',[(30,40,60)],'哈哈')
res=tuple2[3][0]
print(res)
tuple2[3][0]=(60,70)
print(tuple2)
# -------------------常用函数-----------------
# count函数():用于统计元素出现的次数
tuple3=(20,20,30)
res=tuple3.count(20)
print(res)
# index():用于返回元素索引值
res=tuple3.index(30)
sorted()
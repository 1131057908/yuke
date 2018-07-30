# set:集合输一个无序的,元素不可重复的数据组合.
# 他有两个作用:  1  去重  ,把一个容器变成集合,可实现去重功能
#  2.关系测试,测试两组数据之间的交集,差集,并集 等等
list=[1,2,3,4,5,1,1,2,1]
set_1=set(list)
print(type(set_1))
print(set_1)


tuple1=(5,6,7,8,9,8)
set_2=set(tuple1)
print(type(set_2),set_2)

string='黄昏'
set_3=set(string)
print(type(set_3),set_3)

dict={'陈':'c','李':'l'}
set_4=set(dict)
print(type(set_4),set_4,'阿达')


# -------------------常用函数----------------
# 声明一个空集合set集合的时候,一定要注意不要和声明一个空字典搞混淆
# add():注意往集合添加数据,如果重复数据也会自动去重


# 声明一个空集合
myset=set()
# 添加数据直接在add()里面添加
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(1)
print(myset)



# 2.remove();删除集合中的元素,括号中级直接添加要删除的元素的值,如果要删除的元素不在集合中
# 则会报错
myset.remove(1)
print(myset)
# myset.remove(1)
# print(myset)
# myset.remove(1)
# print(myset)
# 3.discard();删除集合中的元素,括号中级直接添加要删除的元素的值,如果要删除的元素不在集合中
# 也不会报错
myset.discard(2)
print(myset)
myset.discard(2)
print(myset)
# pop()  随机删除集合中的元素
# myset.pop()
# print(myset)
# myset.pop()
# print(myset)
# update();会将传入的数据每一个元素随机分别别传入到集合当中变成集合中的一个元素,区别
# add默认会将要传入的数据整体当成一个元素传入到set 集合当中
myset.update('今晚吃鸡')
print(myset)
myset.add('不好意思')
print(myset)


#
# ---------------------关系测试运算----------------
list2=[1,2,3,4,5]
set1=set(list2)
print(type(set1),set1)
set2=set(list2)
print(list2)
# intersection:     求两个集合的交集
res=set1.intersection(set2)
print(res,'555',set1,set2)


# union;求两个集合的并集,重复的数去掉
res2=set1.union(set2)
print(res2,'111',set1,set2)
# difference:求两个集合的差集
res3=set1.difference(set2)

print(res3,'000')


# issubclass();判断xxxx是不是xxx的子集
res5=set1.issubset(set2)
print(res5)

# issuperset():判断xxx是不是xxx的父集  返回的结果是ture 或者false
res6=set1.issuperset(set2)
print(res6)

# isdisjoin():判断xxx与xxx是否没有交集,返回结果是ture或者false
res7=set1.isdisjoint(set2)
print(res7)
# clear 清空命令
myset.clear()
print(myset)

# -------------------听过运算符的形式进行关系测算--------

#
# 交集:&
res8=(set1 & set2)
print(res8)
# 并集:|
res9=set1 | set2
print(res9)
# 差集:-
res10=set1-set2
print(res10,'ppp')


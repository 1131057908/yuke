list1=[1,2,3,4,5,6]

for  num in list1:
  print(num)
while list1.count(num)>1:
    res=list1.remove(num)
    print(res)
# list1.sort()+0
# list2=set(list1)
#----------关系测算----------------
my_set_5={1,2,3,4,5}
my_set_6={4,5,6,7,8}
#1.intersection:求两个集合之间的交集
res=my_set_5.intersection(my_set_6)
print(res)
#2.union:求两个集合之间的并集
res1=my_set_5.union(my_set_6)
print(res1)
#3.different:求两个集合之间的差集
res2=my_set_5.difference(my_set_6)
print(res2,'---')
res3=my_set_6.difference(my_set_5)
print(res3)
#4.issuset:判断xx集合是不是xx集合的子集，返回结果是true或者fasle
res4=my_set_5.issubset(my_set_6)
print(res4)
#5.isssuperset():判断xx集合是不是xx集合的父集，返回结果是true，false
res5=my_set_5.issuperset(my_set_6)
print(res5)
#6.isdisjoint:判断xx集合与xx集合是否有交集，返回结果是true，false
res6=my_set_5.isdisjoint(my_set_6)
print(res6)


#&：交集
res7=my_set_5&my_set_6
print(res7)
#|；并集
res8=my_set_5|my_set_6
print(res8)
#-；差集
res9=my_set_5-my_set_6
print(res9)


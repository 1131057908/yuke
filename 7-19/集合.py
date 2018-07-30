#集合（set）是一个无序的，元素不可重复的数据组合他的标识符{}
#集合的两个作用
#1 去重
#关系测试，测试看两组数据之间的交集，差集，并集等
list1=[1,2,12,132,2,2,1,2,1,5]
set_1=set(list1)
print(type(set_1),set_1)


string='哈哈哈哈'
set_3=set(string)
print(type(set_3),set_3)
#常用函数----------------------------------------------
#声明一个空集合和非空集合有区别
#声明一个空集合
list1=[]
tuple=()
my_dict={}
my_set=set()
#声明一个非空集合
my_set_1={1,2,3}
#add（）向集合中添加数据，如果添加的数据已存在，也会去重
my_set_2=set()
my_set_2.add(1)
print(my_set_2)
#remove（）m,删除集合中指定元素，如果指定元素在集合中不存在，则会报错
my_set_2.remove(1)
print(my_set_2)
#discard()；删除指定元素，该元素不在集合中，也不会报错
my_set_2.discard(2)
print(my_set_2)
#pop（）:随机删除集合中的元素，集合为空则为报错
my_set_3={1,2,3,4,5,61,4,5,7,8}
my_set_3.pop()
print(my_set_3)
#update():如果添加的数据是一个序列，他会将序列中的每一个元素当做集合添加到集合当中
#add（）将序列当做一个整体添加到集合当中
my_set_4=set()
my_set_4.update('你好色')
print(my_set_4)
my_set_4.add('真的吗')
print(my_set_4)
#clear():清空集合
my_set_4.clear()
print(my_set_4)





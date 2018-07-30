# 列表:list
# 元组:tuple
# 字符串:str
# 集合:set
# # --------------------列表转换元组,字符串,集合'-------
# 列表转换成元组
list1=['a','b','c','d']
tup=tuple(list1)
print(type(tup))
print(tup)


# 列表转换成字符串
string=''.join(list1)
print(type(string))
print(string)


# 列表转换成集合,      sep='' 去除空格
set1=set(list1)
print(type(string),string,sep='')


# ---------------------元组转换成 列表 字符串 ,集合---
# 元组转化成列表
tuple=('q', 'w', 'e', 'r')
list2=list(tuple)
print(type(list2),list2)

# 元组转换成字符串

string1='  '.join(tuple)
print(type(string1), string1)

# 元组转换成集合
set2=set(tuple)
print(type(set2),set2)

# ----------------------字符串转成 列表 元组 集合--
# 字符串转换成列表
string8='wasd'
list3=list(string8)
print(type(string8),string8,'黄')

# 字符串转换成元组
# tuple2=tuple(string2)
# print(type(tuple2),tuple2)

# 字符串转换成集合

set3=set(string8)
print(type(set3),set3,'000')

# -----------------------集合转换成字符串,元组 列表-------
# 由于集合是无序的,所以转换出来的元组 字符串 列表是随机的
# 声明一个非空集合
my_set={'z','x','c','v'}
# 声明一个空集合
# my_set=set()
# 集合转换成字符串
string8='  '.join(my_set)
print(type(string8),string8)
#
# 集合转换成列表
list4=list(my_set)
print(type(list4),list4)

# 集合转换成元组
# tuple3=tuple(my_set)
# print(type(tuple3),tuple3)
# ----------------------字符串的添加和修改------


#  修改
string7='你好'
new_string=string7.replace('你','他')
print(new_string)


#添加
# 先将字符串转成列表
new_list=list(string7)
print(type(new_list),new_list)
# 向列表中添加字符
new_list.insert(2,'他')
new_list.insert(3,'也')
new_list.insert(4,'好')
print(new_list)
# 在将列表转回字符串
string20=str.join(new_list)
print(type(string20),string20)

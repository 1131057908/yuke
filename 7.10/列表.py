# 列表;(list)容器性类型的数据,里面可以保存整数,小数,True/False,字符串,列表
# 元组,字典,对象,等等类型的数据,列表是可变的课以增加,删除,修改
# --------------------------
# 创建一个空列表
list1=[]
# 创建一个非空列表
list2=[20,9,88,True,'张三']
# append():括号里直接添加数据 默认添加在末尾
list1.append('李四')
print(list1)
# insert():可以根据元素的索引值插入指定数据  第一参数要插入索引位置
# 第二参数:要插入元素值
# 索引:他是从0开始,一次向后+1的一个整数,用于标记一个元素在容器中的存放位置
# 解释器会给每个元素设置一个索引值,可以根据索引值进行增删改查
# 索引值是唯一的,不可重复
list1.insert(0,'小明')
print(list1)
# -------------------删除数据----------------
list3=['张三','李四',20,False,'哈哈哈']
# pop()函数:根据索引值,删除列表中某一个元素,括号中填写的是索引值
# 如果列表中不填写索引值,默认会删除列表中最后一个元素
list3.pop(4)
print(list3)
list3.pop()
print(list3)
# remove():括号中直接填写要删除的元素,如果要删除的元素在列表中存在多个,在默认删除第一个符合
# 条件的元素
list3.remove('李四')
print(list3)
list4=['张三','李四','麻子','王二','麻子']
list4.remove('麻子')
print(list4)
# del ()也是根据索引值删除元素
del list4[3]
print(list4)
# 使用while循环删除列表中所有元素
# len():获取容器长度
while len(list4):
     del list4[0]
print(list4)
# -----------------------查询----------
# 根据索引值查询
list5=['Uzi','7酱','让帝','司马老贼','狗妃','mlxg']
changzhang=list5[1]
print(changzhang)
# 切片取值,取头不取尾,从索引值为0取到索引值为2
# [头下标:尾下标]
name=list5[0:3]
print(name)
# 从索引值为0元素,取到索引值为5的元素,每次挑两个间隔
name1=list5[0:6:2]
print(name1)
# 如果切片不设置头下标,则默认从0开始取值
name2=list5[:6]
print(list5)
# 如果切片不设置尾下标
name3=list5[0:]
print(name3)
name4=list5[::2]
print(name4)
name5=list5[:]
print(name5)
#倒序取值
list6=['edg','永不团灭','rng','永不言弃']
last=list6[-1]
print(last)
last1=list6[-2]
print(last1)
# 通过for循环查询全部元素
for x in list6:
    print(x)
for y in range (0,len(list6)):
    print('===',list6)
# 通过枚举方法查询
for index,value in enumerate(list6):
    print(list6)
print('牛股迪欧')

list6[-1]='永不言败'
print(list6)
list6[0]='we'
print(list6)
# --------------常用函数---------
list7=['亚索','盲僧','劫','瑞文','维恩','亚索']
# cout():用于统计某一元素在列表中出现的次数
num=list7.count('亚索')
print(num)
# index():用于显示元素索引,如果要查询的元素在列表中存在多个,则默认返回第一个符合条件的元素的索引

print(num1)
num1=list7.index('盲僧')
# reverse()"将列表反转"
list7.reverse()
print(list7)
# sort:对列表的元素进行排序,默认按照ascii码进行排序
list8=[1,2,3]
list9=[4,5,6]
list8.extend(list9)
print(list8)
# clear()清空列表
list8.clear()
print(list8)
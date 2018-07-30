# 字典:也是python中内置的一种容器类型,字典是可变的也可以对字典增删改查的操作
# 字典的特点
# 字典是以'键-值'结构来储存数据,字典没有索引这个概念 键相对于列表中的索引 可以通过键对一个数据
# 进行增删改查
# 列表中索引值是唯一的 键也是唯一的  都不允许重复
# 字典是无序的,键-值 对的储存没有先后顺序,只需一个键对应一个值

# 声明一个空字典
dict1={}
# 计算机内存中True=1,false=0  dict3中1与True发生键冲突   1  0  不能同时为字典的键
# 列表 字典不可当做键  元组可做键  因为通常情况下键不可变 但是列表 字典可变的,但是元组不可变的所以可做键
# 声明一个非空字典1
dict2={'ADC':'UZI','辅助':'ming','打野':'MLXG','中单':'xiaohu','上单':'letMe'}
dict3={1:'1',True:'true',(1,2,3):'(1,2,3)'}
#声明一个、非空字典2
dict2=dict(name='张三',age='20')
# ---------------添加数据-------------------
# 添加数据时,要指定一个键,并且要给该键赋一个值
dict2['替补']='Karsa'
print(dict2)
# --------------------------查询数据---------------
name=dict2['ADC']
print('他的名字是:{}'.format(name),'-----------')
name1=dict2['辅助']
print(name1)
# # --------------------常用函数----------------------
dict4={'name':'张三','age':20,'sex':'男'}
# get () 根据键获取对应的值,如果字典中不存在这个键,则默认采用后面的默认值 返回值是输入值
# 如果存在该键,则直接取字典中的值
res=dict4.get('name','李四')
print('----123456',res)
res1=dict4.get('height','178')
print(res1)
# items()  将字典中每一个键值对设置成元组形式,并且存储在列表中
res2=dict4.items()
print(res2)
# 字典第一种遍历方式
for key ,value in dict4.items():
    print(key,value)
# 字典第二种遍历方式,只去键不取值  相当于遍历(name,age,sex)
for  key,value in enumerate(dict4):
    print('---',key,value)
# keys()  取出字典中的键并存放在列表中
res3=dict4.keys()
print(res3)
# values;取出字典中的值并存放在列表中
res4=dict4.values()
print(res4)
# pop ()   根据键删除字典中的值  返回的结果删除的是这个键对应的值
res5=dict4.pop('sex')
print(res5)
# setdefault;根据键获取对应的值,如果字典中不存在这个键,取输入的值
# 如果存在该键,则直接获取字典中的值,并且将该键值对加入到字典中
dict5={'name':'麻子','age':'21','sex':'女'}
res6=dict5.setdefault('name','王二')
print(res6)
res7=dict5.setdefault('height',188)
print(res7)
print(dict5)
# popitem();随机返回并删除字典中的一对键值对(一般删除末尾键值对)
# 返回值是一个被删除的键值对的元组
res8=dict5.popitem()
print(res8)
print(dict5)
# fromkeys();用于生成一个字典,第一参数是键 第二参数是值
dict6=dict.fromkeys('12',[1,2])
print(dict6)
dict7=dict.fromkeys('1','哈哈哈')
print(dict7)
# update():讲一个字典添加到另一个字典中
dict8={'射手':'Iboy','辅助':'meiko'}
dict9={'打野':'7酱','中单':'Scout','上单':'Ray'}
dict8.update(dict9)
print(dict8)
# in 判断一个键是否在字典中
if '射手' in dict8:
    print('存在射手这个键')
# clear()清除所有键值对
dict8.clear()
print(dict8)
dict10={'name':'张三'}
del dict10['name']
print(dict10)

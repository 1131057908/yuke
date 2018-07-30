#声明一个空字典
dict1={}
#声明一个非空字典
dict2={'adc':'12','spupoter':'34',}
#第二种方法
dict2=dict(name='张三',age='20')


#添加元素
dict2['height']='175'
print(dict2)
#查询元素：提供键
res=dict2['name']
print(res)
#get()根据键取出对应值，如果字典中有这个键，则直接取出，不存在这个键，
#则会输出 该键对应的值
res2=dict2.get('weight','66')
print(res2)
res3=dict2.get('name','黄')
print(res3)
#items() 将字典中的每一个键值对设置成元组的形式，存在列表中
res4=dict2.items()
print(res4)
#第一种遍历
for key , value in dict2.items():
    print(key,value,'000')
for tuple_test in dict2.items():
    print(tuple_test[0],tuple_test[1],'111')
for key , value in enumerate(dict2):
    print(key,value,'222')
#key()取出所有键，并存放在列表中
# res5=dict2.key()
# print(res5)
#values()取出字典中的值，并存放在列表中
res6=dict2.values()
print(value)
#pop()  根据键删除字典中的值，并返回这个值
# res7=dict2.pop()
# print(res7)

#setdefault() 如果存在该键，则直接获取字典中所对应的值，如果不存在该键，采用后面的值，并直接添加
res8=dict2.setdefault('hao','黄')
print(res8)


#popitem()随机删除字典中的一对键值对，返回值是由键值对组成的元组

#fromkey()生成一个字典，第一参数是键，第二参数是值，第一参数是可迭代对象，则会将对象中的每一个元素当做键，并且把第二参数当做每一参数的值
dict5=dict.fromkeys([1,2],[7,8])
print(dict5)
# update()  合并两个字典
dict2.update(dict5)
print(dict2)
# del 根据键删除字典中的值
#in判断一个键在字典中
if 'name' in dict2:
    print('zai')
#clear()
dict2.clear()
print(dict2)


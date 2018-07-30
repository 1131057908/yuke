##字典是python z中一中容器类型 可变，可进行增删改查
#字典是以键值对存储数据  没有索引 ，键相当于索引
#通过键对数据进行增删改查
#列表和元组的索引值是唯一的 键也是唯一的
#字典是无序的，键值对的存储无线后，zhixuy一个键对一个值
#声明一个空字典
dict1={}
#声明一个空字典
# dict_lol={'ADC:李玉恒','辅助':刘家豪,'打野':有效,'中单':}
#----------查询数据-----------】
# x=dict_lol['ADC']
# print(x)
#
#
# #-------------x常用函数---------
# #get()  第一参数：键  第二参数：默认值
# res=dict_lol.get[name；娜娜]#name 后面有原来值  则会采用原来值
# res=dict_lol.get[huoli:100]#没有的新元素则会输出100
# items()；将字典每一个键值对设置成元组的形式，并存放在列表中
#
#
#
# #遍历的方法
#
# for tuple_test in dict_lol.items():
#       print(tuple_test[0],tuple_test[1])
#
dict_lol={'ADC':'李宇恒','辅助':'刘家豪','打野':'游晓','中单':'高茂远','上单':'李洪涛'}
res=dict_lol.get('ADC','欧阳臣')
res1=dict_lol.get('教练','马森')
print(res,res1,dict_lol)

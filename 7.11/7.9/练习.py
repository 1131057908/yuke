# if 条件句 的 偶奇数判断 和 倍数
# num=input('请输入数字:')
# num=int(num)
# if num % 2 == 0:
#     print('该数字是偶数')
# else:
#     print('该数字是奇数')
# if num % 12 ==0:
#     print('该数字是三和四的倍数')
# else:
#      print('该数字不是三和四的倍数')
##################################
# 产生 randint 范围内 的 随机数字
# from random import randint
# num=randint(10,156)
# print(num)
###################
# for index in range (1314,1315):
#     print('I LOVE YOU ')
#     print('笔芯')
# sum=0
# for x in range(1,101):
#     sum+=x
# print(sum)
# ji_he=0
# bei_he=0
# for index in range (1,101):
#     if index % 2 ==1:
#        ji_he+=index
#     if index % 5==0:
#         bei_he+=index
#     result=ji_he+bei_he
# print(result)
# 石头0  剪刀1  布2  人 -1   win    ,computer  2




#
# from random import  randint
# user_win=0
# computer_win=0
# deuce=0
# # index 代表标号,value代表值
# for index,value  in enumerate (range(3)):
#     user_num=input('请输入数字')
#     user_num=int(user_num)
#     computer_num =randint (0,2)
    # if  user_num-computer_num==-1:
    #     print('user_win')
    # if user_num-computer_num==0:
    #     print('duce')
    # if user_num-computer_num==2:
    #     print(computer_win)
    # if user_num-computer_num==-1 or user_num-computer_num==2:
    #       print('第{}局玩家胜'.format(index+1))
    # elif user_num-computer_num==0:
    #     print('第{}局平局'.format(index+1))
    # else:
    #     print('第{}局电脑胜'.format(index+1))
    # if user_win==2:
    #     print('user win')
    #     break
    # if computer_win==2:
    #     print('computer win')
    #     break
    # else:
    #       if deuce==1 and user_num-computer_num==0 and index==2 :
    #         print('平局')
    #       elif deuce==3:
    #         print('平局')
    #       elif deuce==2 and index==2  :
    #         if user_num-computer_num==1:
    #          print('user win')
    #       else :
    #          print('computer  win')
# for x in range (1314,1315):
#    print(x)
# age=0
#  for x in range (18):
#      print('未成年人,今年{}岁'.format(x))
#    x+=1
# while age < 17:
#
#     age+=1
#
# print('未成年人,今年{}岁'.format(age))
# index=1
# while  index <10:
#     index+=1
# if index==4:
#  pass
#
#  print(index)

# info = '今天是星期四 Hello World'
# print(info[7])
# # 获取指定内容  切片操作
# # 值1：开始位置 （包括该位置）
# # 值2：结束位置  （不包括该位置）
# print(info[3 : 5])
# # IndexError: string index out of range
# # 索引错误：字符换索引超出范围
# # print(info[100])
# # 当范围超出边界的时候
# # 直接获取从指定开始到字符串结束的部分
# print(info[3:100])

# info = '2018七月七,我在智游吃炸鸡'
# # 获取从指定位置到结束位置的内容
# print(info[3:])
# # 反序截取字符串
# print(info[:-3])
# # 相当于直接获取info的整个内容
# print(info[:])
# print(info[:3])
# num = 'abc'
# if num.isdigit() :
#     print('22')
#     # '1'  '2'  '100'
#     num = int(num)
# else:
#     print('00')
    # '-1' , '-1000'  1000
    # num = num[:]
    # print(num)
    # num = int(num)
    # num = num * -1
    # print(num)
# a = '123567'
# for i in '-123abc567':
#     if i.isdigit():  #'1' '2'
#         a += i
# a = int(a)   #123567
# print(a)a = '123567'
# for i in '-123abc567':
#     if i.isdigit():  #'1' '2'
#         a += i
# a = int(a)   #123567
# print(a)


# i='123abd456'
# if  i.isdigit():
#  i=int(i)
# print('1234567')
# else:
# s = input('请随便输入：')
# for i in range(0, len(s)):
#     if s[i].isdigit():
#         print(s[i])
#     else:
#         pass
# s= input('请输入:')
# for i in range(0,len(s)):
#     if s[i].isdigit(0):
#         print(s[i])
#     else:
#         pass
#
# i='123abd456'
# if  i.isdigit():
#  i=int(i)
# print('1234567')
# class People(object):
#   def __init__(self,name='',sex=False,age='',height=''):
#      self.name=name
#      self.sex=sex
#      self.age=age
#      self.height=height
#   def isFitMe(self,other):
#    if self.sex==other.sex:
#     print('你我同性')
#     return
#     if self.age-other.age==5:
#      print('小朋友')
#     return
#     if  other.height<180:
#       print('我喜欢大长腿')
#     return
# print('喜结良缘')
# cuiying=People('崔颖',False,18,160)
# zhangsheng=People('张生',True,20,181)
# cuiying.isFitMe(zhangsheng)


#
# import sqlite3
# con=sqlite3.connect('myDB')
# cursor=con.cursor()
# cursor.execute('CREATE TABLE  IF NOT EXISTS my_info(name text,xuehao int,fond text)')
# con.commit()
# cursor.execute('INSERT INTO my_info(name,age,fond)VALUES("天天","12","网球")')
# con.commit()
# cursor.execute('INSERT INTO my_info(name,age,fond) VALUES ("小鱼","14","游戏",)')
# con.commit()
# cursor.execute('INSERT INTO my_info()')
# cursor.execute('DELETE FROM my_info WHERE  fond="游戏"')
# con.commit()
# 原码,反码,补码
# 原码:规定了字节数,写明了符号位,就得到了数据的原码
# 1000000000000000000000000001
# 反码:正数的反码是期原码,
# 0000000000000000000000000001
# 0000000000000000000000000001
# 负数的反码是其原码的符号位不动,其他位取反
# 1000000000000000000000000001
# 1111111111111111111111111110
# list=['吃饭','睡觉','打豆豆']
# list.insert (0,'喝水')
# print(list)
# list.pop(0)
# print(list)
# list.remove('睡觉')
# print(list)
# for x in range(0,10):
#  for y in range(1,x+1):
#   print('%d*%d'%(x,y),end ='  ')
#  print('')
# print(3+5)
# print('3'+'5')
# for x in range (1,10):
#  for y in range(1,x+1):
#   print('%d*%d=%-5d'%(y,x,x*y),end='')
#  print('')
#猜数字游戏
# #random python 中一个随机模块
# import random
# #第一步生成随机整数,
# random_number =random.randint(0,10)
# #定义一个整数,记录错误次数,
# error_count=0
# while True:
# #input函数接受是字符串类型,想要和整数作比较,需要进行转换变量的类型
#   #通过while不断检测输入的数字是否符合要求,如果不符合要求则提示用户重新输入
#   input_number=int(input('请输入要猜的数字:'))
#   while input_number<0 or input_number>10:
#     input_number=int(input('输入错误,请您后重新输入:'))
#   if input_number>random_number:
#       print('不好意思猜错了')
#       error_count+=1
#   if input_number<random_number:
#       print('不好意思猜小了')
#       error_count+=1
#   if error_count>3:
#    print('您的机会用尽')
#    error_count+=1
#   if input_number==random_number:
#     print('''
#     恭喜您猜对了
#     1-继续猜
#     2-退出
#     ''')
#     error_count==0
#     select_number=int(input('请您选择要操作的序号:'))
#     while select_number!=1 and select_number!=2:
#        select_number=int(input('输入错误,请您重新输入:'))
#     if select_number==1:
#        random_number=random.randint(1,10)
#     else:
#         break
#     if error_count>=3:
#      print('您的机会已用完')
#      break
# 列表(关键字:list),容器类型数据,里面可以存储各种数据,比如:整数,小数,字符串,布尔值True/false
# 列表 元组 字典等 可以进行增删改查
# --------------------创建列表-*------------------
# 创建一个空列表
list1=[]
# 创建一个非空列表
list2=['张三','李四','20','20.55',True,[1,2,3]]
# ------------------------想列表中添加元素------------
#append():括号中填写的是要添加的元素.默认添加到列表末尾
list1.append('麻子')
print(list1)
list1.append('张三')
print('list1')
#insert()  可通过元素索引值插入指定位置,第一参数插入位置即索引值  第二参数:插入的元素
#索引是从零开始往后依次加一,用于标记在容器中存放的位置,解释器会默认给每一个元素设置一个索引,可以根据索引值进行增删改查,索引值唯一,不可重复

list1.insert(1,'李四')
print(list1)
#-------------------------删除列表中的数据--------------
list3=['z张三','小明','小红','小刚']
#pop() 根据索引值删除列表中某一个元素,括号中填写的是要删除的元素的索引值,不填索引值默认删除最后一个
list3.pop(0)
print(list3)
#remove(): 括号中直接填写要删除的元素,如果要删除的元素在列表中存在多个相同,则默认会删除符合条件的第一个元素

list3.remove('小红')
print(list3)
list4=['小红','小明','小刚','小红']
list4.remove('小红')
print(list4)
#del()根据索引值删除元素,括号添加要删除的元素的索引值
del list4[1]
print(list4)
#使用循环删除列表中所有元素
#len()获取容器长度
print(len(list4))
while len(list4):
    del list4[0]
    print(list4)
#--------------------查询------------
list5=['白帅康','蔡飞','陈罗文','陈鹏']
caifei=list5[1]
print(caifei)
chenpeng=list5[3]
#切片取值.[头下标:尾下标],取头不取尾[0:3]=0,1,2 从索引值为0 取到索引值为2的数据切片取值类型不变

print(chenpeng)
name=list5[0:3]
print(name)
#从索引值为0的位置取到索引值为5的位置,每次跳2个索引值
name2=list5[0:6:2]

#切片取值如果不设置尾下标默认取到最后
name3=list5[0:]

#切片不设置头下标 也不设置尾下标默认取出全部元素
name4=list5[:]

#从列表中索引为零的位置取到最后,每次跳2个索引
name5=list5[::2]


#切片倒叙取值
last_name=list5[-1]

name6=list5[-5:-1:2]
print(name6)

#使用for循环查询所有的元素
for x in list5:
    print(x)
#根据索引值遍历所有元素
for y in range(0,len(list5)):
    print(y,list5[y])
#使用枚举函数enumerate(),可以吧索引值和对应的元素都查询出来
for index, value in enumerate(list5):
    print('索引值:%s,元素;%s'%(index,value))

#
# ----------------------修改列表中的值---------------
list5[0]='小明'
print(list5)
list5[-1]='小明'
#------count:统计某一元素在容器中的出现的次数-
num=list6.count('亚索')

#index:()  用于显示元素索引,若存在多个则默认返回第一个符合条件的元素
num1=list6.index()

reverse

list7.extend list6

for x in list10:
    list11.append (x)
clear()
"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:文件读写.PY
@ide:PyCharm
@time:2018-07-20 10:47:41
"""
#大象装进冰箱 1-打开冰箱2-吧大象装进去3-guanmebn
# 文件读写：1-打开文件2-对文件进行读写3-关闭文件
#



#
# #1.打开文件
# #opem*()第一参数：文件名 第二参数：文件打开方式 第三参数：文件编码方式 这三个位置不可变
# #文件打开的模式
# #1.w ：只写模式，会对文件覆盖写入

#  r:只读模式，如果打开文件，文件不存在。则会报错，存在直接打开

#w+: 写读模式，如果文件不存在，则会自动创建，如果存在直接打开
#使用open打开的时候会清空文件,光标在文件开头位置,会对文件覆盖写入

# # r+；读写模式，文件不存在报错，存在直接打开,区别于w+  直接open打开不会清空
# 如果光标不在文件末尾，会覆盖源文件元素，不会完全覆盖，会根据光标写入位置覆盖


#  a  a; 追加只写模式,文件不存在直接创建，存在直接打开
#如果文件是空的会从文件开头位置，不为空光标会在末尾位置。无论光标在哪都会在末尾添加上字符


#a+ ：追加读写模式，文件不存在自动创建，存在直接打开不为空光标会在末尾位置。无论光标在哪都会在末尾添加上字符






# ---------------------w只写模式------------------

# f = open('test,txt','w',encoding='utf-8')
# #1.writable():判断文件是否可写，返回结果是true，false
# print(f.writable())
# #2.readable（）判断文件是否可读返回结果是true ,false
# print(f.readable())
# #3.tell():返回当前位置
# print(f.tell)
# f.write('123')
# print(f.tell())
# #4.name():返回文件名
# print(f.name)
# #5.encoding:返回当前文件的编码格式
# print(f.encoding)
# #6.seek（）；返回到指定光标位置
# f.seek(1)
# print(f.tell())
# f.write('456')
#
#
#
# f.close()#关闭文件，因为文件写入首先写入计算机缓存中，后写入硬盘里，假如文件未关闭，遇到突发状况，入关机，会导致文件损坏




#------------------r 只读模式---------------

# f=open('test1,txt','r',encoding='utf-8')
# print(f.tell())
# print(f.readable())
# print(f.writable())
# #read()读取文件’如果read（）不填参数，则默认读取这个内容
# # print(f.read())
# # print(f.tell())
# # f.seek(0)
# # print(f.read(5))
# print(f.readline())#readline（）只读一行
# # print(f.readlines())#readlines（）会读取多行，但会吧每一行的数据当做一个元素存放在列表中
#
# f.close()

# --------------w+写读模式------------
#
# f=open('test2,txt','w+',encoding='utf-8')
# print(f.tell())
# print(f.readable())
# print(f.writable())
# f.write('456')
# f.seek(0)
# print(f.read(1))
# f.close()


#--------------r+ 读写模式-----------------
# f=open('test3,txt','r+',encoding='utf-8')
# print(f.tell())
# print(f.readable())
# print(f.writable())
# print(f.read(3))
# print(f.tell())
# f.write('haha')
# print(f.tell())
# f.seek(5)
# f.write('bbb')
# f.close()



#-------------  a   追加只写模式---------------
# f=open('test4,txt','a',encoding='utf-8')
# print(f.tell())#光标在文件开头位置
# print(f.readable())
# print(f.writable())
# f.write('ccc')
# print(f.tell())
# f.seek(2)
# f.write('000')
# # print(f.tell())
# f.close()


#----------------a+ 追加读写模式-----------
# f=open('test5,txt','a+',encoding='utf-8')
# print(f.tell())
# print(f.writable())
# print(f.readable())
# f.seek(0)
# print(f.read(5))
# print(f.tell())
# f.write('8888')
# print(f.tell())
# f.seek(5)
# f.truncate(3)
# print(f.tell())
# f.close()
#------------------------------trucate------------
#trucate
# f=open('test6,txt','a+',encoding='utf-8')
# print(f.tell())
# f.seek(2)
# #trucate():指定从开头到指定长度，其余内容删除，不指定长度，就从文件开头截止到当前位置，其余内容删除
# f.truncate(3)
# f.close()


#--------------------flush-----------------
# f=open('test7,txt','a+',encoding='utf')
#一些总结：一般的文件操作流程包含缓冲机制，“write'方法并不直接将数据写入文件，而是首先写入内存中特定缓冲区，
#flush方法将缓冲内容写入文件，至于close原理是内部先调用flush方法来刷新缓冲区，在执行关闭操作，这样即使缓冲区数据未满也能保证数据完整性
#如果进程出现意外未执行close缓冲区内容将丢失




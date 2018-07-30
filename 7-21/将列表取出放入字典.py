# coding:utf-8
# """
# 座右铭:吃饱不饿，努力学习
# @project:预科
# @author:Mr.Huang
# @file:将列表取出放入字典.PY
# @ide:PyCharm
# @time:2018-07-21 09:24:41
# """
# # 网址提取。手机通讯录 ， k1k2
# #手机通讯录
# list_student=['郝超杰','李威','李四','张广师','李宇恒','池永伟','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪']
# #声明一个空字典
# student_dict={}
# for student in list_student:
#     fist_char=student[0]
#     if fist_char in student_dict:
#         res_list=student_dict[fist_char]
#         res_list.append(student)
#     else:
#         res_list=[student]
#         student_dict[fist_char]=res_list
# while True:
#     print('''
#     1-查询
#     2-退出
#     ''')
#     select_num=int(input('请输入操作序号：'))
#     while select_num!=1 and select_num!=2:
#         select_num=int(input('输入操作序号错误，请您重新输入：'))
#     if select_num==1:
#         name_char=input('请输入查询的姓氏：')
#         if name_char in student_dict:
#             stu_list=student_dict[name_char]
#             for index,value in enumerate(stu_list):
#                 print(index+1,'-',value)
#         else:
#             print('没这人')
#     else:
#         break


#网址提取训练
# string='<div class="item-list ni-list"><ul><li  class="first"><a href="http://www.tepintehui.com/detail/57185?ce" title="明星同款| 钟基欧巴穿的小脏鞋5折辣!" ><span>明星同款| 钟基欧巴穿的小脏鞋5折辣!</span></a></li><li><a href="http://www.tepintehui.com/detail/56847?ce" title="装逼| 你们见过凌晨四点钟的洛杉矶吗?" ><span>装逼| 你们见过凌晨四点钟的洛杉矶吗?</span></a></li><li  ><a href="http://www.tepintehui.com/detail/57127?ce" title="反人类| 世界上最干净的纸竟然是黄色的!" ><span>反人类| 世界上最干净的纸竟然是黄色的</span></a></li><li><a href="http://www.tepintehui.com/detail/57120?ce" title="科普| 吃了避孕药之后怀的孩子能要吗?" ><span>科普| 吃了避孕药之后怀的孩子能要吗?</span></a></li><li><a href="http://www.tepintehui.com/detail/57125?ce" title="真假| 9年义务升为12年制,是要取消高考吗" ><span>真假| 9年义务升为12年制,是要取消高考吗</span></a></li><li><a href="http://www.tepintehui.com/detail/57124?ce" title="土豪| 揭秘迪士尼见不得光的33号俱乐部" ><span>土豪| 揭秘迪士尼见不得光的33号俱乐部</span></a></li><li  ><a href="http://www.tepintehui.com/detail/41008?ce" title="吐槽| 男人单身太久会没感觉?" ><span>吐槽| 男人单身太久会没感觉?</span></a></li><li  ><a href="http://www.tepintehui.com/detail/23488?ce" title="冷知识| 为什么镜子是左右颠倒不是上下呢" '

#声明两个变量，记录要查找的起始字符串和终止字符串
# start_mark='href="'
# end_mark='/detail/'
# record_position=0
# while record_position<len(string):
#     start_index=string.find(start_mark,record_position)
#     if start_index==-1:
#         break
#     end_index=string.find(end_mark,start_index)
#     url=string[start_index+len(start_mark):end_index]
#     record_position=end_index
#     print(url)
# list1=string.split('"')
# print(list1)
# for x in list1:
#
#     if x[0:4]=='http':
#        print(x)

#-------------------------------------
# string="k:1|k1:2|k2:3|k3:4"
# dict1={}
# list1=string.split('|')
# print(list1)
# for x in list1:
#     res=x.split(':')
#     print(res)
#     dict1[res[0]]=res[1]
# print(dict1)

# string="k:1|k1:2|k2:3|k3:4"
# res=string.replace(':','|')
# print(res)
# res2=res.split('|')
# print(res2)
# dict1={}
# for x in range (len(res2)):
#     if x %2==0:
#         dict1[res2[x]]=int(res2[x+1])
# print(dict1)

#---------------------------------------------------
# w=input()
# dict1={}
str='sunk is a good man   sunk is a good man  sunk is a good man sunk is a good man   sunk is a good man sunk is a good man  sunk is a good man  sunk is a good man !'
# list1=str.split(' ')
# # print(list1)
# for x in list1:
#     # print(x)
#     res=dict1.get(x)
#     # print(res)
#     if res==None:
#         dict1[x]=1
#         # print(dict1)
#     else:
#         dict1[x]=dict[x]+1
#         print(dict1)
# print(dict1[w])


# list2=list(str)
# print(list2)
# list1=str.split(' ')
# print(list1)
# res5=list1.count('is')
# # res4=list2.count('is')
# print(res5)
print('')



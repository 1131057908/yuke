# # grade=int(input('请输入成绩'))
# # if grade<60:
# #     print('不及格')
# # elif grade>=60 and grade<70:
# #     print('等级是D')
# # elif grade>=70 and grade<80:
# #     print('等级是C')
# # elif grade>=80 and grade <90:
# #     print('等级是B')
# # elif grade >=90 and grade<=100:
# #     print('等级是A')
#
#
# # 已知一个人的身高是180，体重是80公斤，计算一个人的最佳体重
# # 最佳体重计算公式：
# # 最佳体重 = 身高 - 105
# # 通过体重和最佳体重的对比，利用print输出此人是体重正常还是偏胖还是偏瘦。
#
# # height=180
# # weight=80
# # 最佳体重= height-105
# # if weight / 最佳体重>1:
# #     print('体重偏胖')
# # if weight / 最佳体重<1:
# #     print('体态偏瘦 ')
# # if weight / 最佳体重==1:
# #     print('体重正常')
# # class People(object):
# #  def __init__(self,name='',age='',height='',weight='',income='',sex=''):
# #      self.name=name
# #      self.age=age
# #      self.height=height
# #      self.weight=weight
# #      self.income=income
# #      self.sex=sex
# #  def isFitMe(self,other):
# #      if self.sex==True and self.sex==other.sex:
# #          print('都是汉子,性别相同')
# #          return
# #
# #      if other.height < 160 or other.height > 175:
# #
# #          print('身高不合适')
# #          return
# #      if other.weight < 40 or other.weight > 60:
# #          print('体重不合适')
# #          return
# #
# #      if other.income < 2000 or other.income > 5000:
# #          print('工资不合适')
# #          return
# #      print('喜结良缘')
# #
# #      if other.age < 20 or other.age > 28:
# #          print('年龄不合适')
# #          return
# # cancan=People()
# # baobao=People()
# # cancan.sex=input('请输入性别:')
# # cancan.age=input('请输入年龄:')
# # cancan.height=int(input('请输入身高:'))
# # cancan.weight=int(input('请输入体重:'))
# # cancan.incom=int(input('请输入收入:'))
# # cancan=People(True,20,162,50,3000)
# # # cancan=People(input('请输入性别:'),input('请输入年龄:'),input('请输入身高:'),input('请输入体重:'),input('请输入收入:'))
# # baobao=People(False,20,178,65,5000)
# # baobao.isFitMe(cancan)
# #
#
# # while True:
# #     km = int(input('请输入公里数'))
# #     while km<=0:
# #         km = int(input('输入正确公里数,请重新输入:'))
# #     if km<=2:
# #         cost=8
# #
# #     if km>2 and km<12:
# #         cost=(km-2)*1.2+8
# #
# #     if  km>12:
# #         cost=(km-12)*1.5+10*1.2+8
# #             print('cost')
# # stu=[]
# # while True:
# #     print('''
# #        1.添加学员
# #        2.修改学员姓名
# #        3.查询学员姓名
# #        4.删除学员姓名
# #        0.退出程序
# #        ''')
# #     shuru_number=int(input('请选择功能'))
# #     if  shuru_number==1:
# #         stu.insert(input('请输入索引值'),input('请输入添加学员姓名'))
# #         print(stu)
# #     elif shuru_number==3:
# #         chaxunxingming=stu[input('请输入姓名')]
# #         print(chaxunxingming)
# #     elif shuru_number==2:
# #         stu[input('请输入索引值')]=input('请输入修改的名字')
# #         print(stu)
# #     elif shuru_number==4:
# #         stu.remove(input('请输入删除的姓名'))
# #     print(stu)
# #     elif shuru_number== 0:
# #     print('退出程序')
# #
# # 学员管理系统
# # 声明一个学员保存信息的列表
# member_list=[]
# while True:
#   print('''欢迎python13期学员信息管理系统
#   1-添加学员姓名
#   2-修改学员姓名
#   3-查询学员姓名
#   4-删除学员姓名
#   0-退出
#   ''')
#   select_number=int(input('请选择您选择的序号:'))
#   while select_number<0 or select_number>4:
#       select_number=int(input('序号输入错误,请重新输入:'))
#   if select_number==1:
#       name=input('请输入要添加的学员的姓名')
#       member_list.append(name)
#       print('学员信息添加成功')
#   if select_number==2:
#       if len(member_list):
#            for x in range(0,len(member_list)):
#                print(x+1,member_list[x])
#            student_num=int(input('请输入要修改的学员序号:'))
#             while student_num<0 or student_num>len(member_list):
#                 student_num=int(input('序号错误,请重新输入修改序号:'))
#             new_name=input('请输入修改的姓名:')
#             member_list[student_num-1]=new_name
#             print('学员信息修改成功')
#       else :
#          print('学员信息为空,无法修改!')
#
#   if select_number==3:
#       if len(member_list):
#          print('''1-输入序号查询
#                   2-查询所有学员''')
#          select_number=int(input('请输入你要操作的序号:'))
#          while select_number!=1 or select_number!=2:
#              select_number=int(input('序号错误,请重新输入序号'))
#       if select_number==1:
#              studen_number=int(input('请输入查询序号'))
#              while student_num<0 or student_num>len(member_list):
#                 student_num=int(input('输入错误;请重新输入:'))
#              name=member_list[student_num]
#              print('查询到的姓名是:%s'%name )
#       if select_number==2:
#              for x in range (0,len(member_list)):
#                  print(x+1,member_list[x])
#   else:
#      print ('学员信息为空,无法查询')
#   if select_num=4:
#     if len(member_list):
#
#       print('''
#       1-输入序号删除
#       2-输入学员姓名删除
#       3-删除所有学员
#       ''')
#     while select_number.
#     else:
#       print('学员信息为空无法删除')
#
#
#
#
#
#
#
#

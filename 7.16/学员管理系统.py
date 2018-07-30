#声明一个学员列表
student_list=[]


while True:
     print(''''
     1-添加学员姓名:
     2-修改学员姓名:
     3-查询学员姓名:
     4-删除学员姓名:
     0-退出
     ''')
     select_number=int(input('请输入操作序号:'))
     while select_number<0 or select_number>4:
         select_number=int(input('输入错误,重新输入'))
     if select_number==1:
         name=input('请输入要添加的学员姓名:')
         student_list.append(name)
         print('学员添加成功')
     if select_number==2:
         #查询列表中是否有学员
         if len(student_list):
             for x in range (0,len(student_list)):
                 print(x+1,student_list[x])
             select_number=int(input('请输入要修改学员的序号:'))
             while select_number<1 or select_number>len(student_list):
                 student_list=int(input('重新输入学员序号:'))
             new_name=input('请输入要修改的姓名:')
             student_list[select_number-1]=new_name
             print('学院信息修改成功')
         else:
             print('学员信息为空,无法查询')
     if  select_number==3:
         if len(student_list):
            print('''1-输入序号查询
                 2-查询所有学员
                 ''')
            select_number=int(input('请输入操作序号:'))
            while select_number!=1 and  select_number!=2:
                 select_number=int(input('输入操作序号错误,请重新输入:'))
            if select_number==1:
                stu_number=int(input('请输入查询序号:'))
                name=student_list[stu_number-1]
                print('查询到的姓名是:%s'%name)
            if select_number==2:
                for x in range (0,len(student_list)):
                  print(x+1,student_list[x])
         else:
             print('学员信息为空,无法查询')
     if select_number==4:
         if len(student_list):
             print('''
             1-输入序号删除
             2-输入姓名删除
             3-删除所有学员
             ''')
         for x in range (0,len(student_list)):
             print(x+1,student_list[x])
         select_number=int(input('请输入操作序号:'))
         if select_number!=1 and select_number!=2 and select_number!=3 :
             select_number=int(input('请重新输入操作序号:'))
         if select_number==1:
             select=int(input('请输入删除序号:'))
             while select<1 and select>(0,len(student_list)):
                 select=int(input('输入序号错误,请重新输入序号:'))
             student_list.pop(select-1)
             print('删除学员成功')
         if select_number==2:
             name=input('请输入删除学员的姓名:')
             while name  not in student_list:
                 name=input('重新输入删除学员的姓名:')
             student_list.remove(name)
             print('删除学员成功')
         if  select_number==3:
             while len(student_list):
                 del student_list[0]
             print('学员信息为空无法删除')
     if select_number==0:
         break






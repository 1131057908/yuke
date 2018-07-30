#声明一个用于保存学员信息的列表
member_list=[]
while True:
    print('''
    1-添加学员
    2-修改学员姓名
    
    3-查询学生姓名
    4-删除学员姓名
    0-退出
    ''')
    select_number=int(input('请输入操作序号:'))
    while select_number<0 or select_number>4:
       select_number=int(input('输入错误请再次输入:'))
    if  select_number==1:
       name=input('请输入姓名:')
       member_list.append(name)
       print('学员信息添加成功')
    if select_number==2:
        if len(member_list):
            for x in range(0,len(member_list)):
               print(x+1,member_list[x])
            student_num=int(input('请输入你要修改的序号:'))
            while student_num<1 or student_num>len(member_list):
                student_num=int(input('序号错误,请重新输入你要修改的学员序号'))
            new_name=input('请输入修改的名字:')
            member_list[student_num-1]=new_name
            print('学员信息修改成功')
        else:
            print('学员信息为空,无法修改')
    if select_number==3:
        if len(member_list):
            print('''
            1-输入序号查询
            2-查询所有学员
            ''')
            select_number=int(input('请输入你要操作的序号:'))
            while select_number!=1 and select_number!=2:
                select_number=int(input('输入操作序号错误,请重新输入:'))
            if select_number==1:
                student_num=int(input('请输入要查询学员的序号:'))
                while student_num<1 or student_num>len (member_list):
                    student_num=int(input('输入序号错误,请重新输入:'))
                    name=member_list[student_num-1]
                    print('查询到的学员姓名是:%s'%name)
            else:
                print('学员信息为空,无法查询')
        if select_number==4:
            if len(member_list):
                print(''''
                1-输入序号删除
                2-输入学员姓名删除
                3-删除所有学员
                ''')
                for x in range (0,len(member_list)):
                    print(x+1,member_list[x])
                select_number=int(input('输入操作序号;'))
                while select_number!=1 or select_number!=2 or select_number!=3:
                    select_number=int(input('输入操作序号错误请重新输入'))
                if select_number==1:
                    select_number=int(input('请输入删除序号:'))
                    while select<1 or select >len(member_list):
                        select=int(input('编号不存在,请重新输入'))
                        member_list.pop(select-1)
                        print('删除学员')
                if select_number==2:
                    name=input('请输入要删除的姓名:')
                    while name not  in  member_list:
                        name=input('请重新输入要删除学员的姓名:')
                        member_list.remove(name)
                        print('学员信息删除成功')
                if select_number==3:
                    while len(member_list):
                        del member_list[0]
                    print('学员信息删除成功')
            else:
                print('学员信息为空,无法删除')
        if select_number==0:
            break
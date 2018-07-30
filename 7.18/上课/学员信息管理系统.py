

member_list=[]
while True:
    print('''
    欢迎使用Pthon-13学员管理系统
    1-添加学员
    2-修改学员
    3-查询学员
    4-删除学员
    0-退出
    ''')
    select_number=int(input('请输入操作选项：'))
    while select_number not in range (1,5):
        select_number=int(input('输入错误，请重新输入：'))
    if select_number==1:
        name=input('请输入要添加的姓名：')
        member_list.append(name)
        print('学员添加成功')
    elif select_number==2:
        if len(member_list):
           for x in range (0,len(member_list)):
             print(x+1,member_list[x])

           student_num=int(input('请输入要修改的序号：'))

           while select_number not in (0,len(member_list)):
               student_num = int(input('输入错误，请输入要修改的序号：'))
           new_name=input()
           member_list[student_num-1]=new_name
           print('修改成功')
    elif student_num==3:
        if len(member_list):
            print('''1-输入序号查询
            2-查询所有学员信息
            ''')
            select_number=int(input())
            while select_number not in range(1,3):
                select_number=int(input())
            if select_number==1:
                select=int(input())
                while select not in len(member_list):
                   select=int(input())
                   result=member_list[select-1]
                   print(result)
            if select_number==2:
                for x in range(0,len(member_list)):
                    print(x+1,member_list[x])
        else:
            print('学员信息为空')
    elif select_number==4:
        if len(member_list):
            print('''
            1-输入学号删除
            2-输入姓名删除
            3-删除所
            有学员
            ''')
        for x in range(0,len(member_list)):
            print(x+1,member_list[x])
            select_number=int(input())
        while select_number not in range(1,4):

            select_number=int(input())
        if select_number==1:
            student_num=int(input())
            while student_num not in len(0,member_list):
                student_num=int(input())
            member_list.pop(student_num-1)
            print('删除成功')
        elif select_number==2:
           name=input()
           while  name not in member_list:
               name=input()
           member_list.remove(name)
           print('删除成功')
        elif select_number==3:
            member_list.clear()
            while len(member_list):
                del member_list[0]
                print()
        else:
            print()
    else:
        break




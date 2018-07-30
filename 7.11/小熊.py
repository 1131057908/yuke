# dict ={'san':'s','hun':'h','den':'d'}
# res=dict.get('san','黄昏')
# print(res)
# res1=dict.get('le','l')
# print(res1)
# dict['eng']='e'
# print(dict)
# res2=dict.items()
# print(dict)
# for key,value in dict.items():
#     print(key,value)
# for key,value in enumerate(dict):
#     print(key,value)
# res5=dict.pop('san')
# print(res)
# res6=dict.setdefault('san','rr')
# print(res)
# res7=dict.setdefault('chen','cc')
# print(res7)
# res=dict.fromkeys('1','[1,2]')
# print(res)
# dict1={'陈':'chen','ling':'mg'}
# dict.update(dict1)
# print(dict)
# del dict['陈']
# print(dict)
# dict.clear()
# print(dict)
#
# **************************************/********************
# 声明一个用于保存学员信息的列表
member_list=[]
while True:
    print('''欢迎使用教务系统
    1-添加学生姓名
    2-修改学生姓名
    3-查询学生姓名
    4-删除学生姓名
    ''')
    select_num=int(input('请输入操作的序号'))
    while select_num<0 or select_num>4:
        select_num=int(input('输入序号错误,请重新输入正确序号'))
    if select_num==1:
            name=input('请输入要添加的姓名')
            member_list.append(name)
            print('添加学生姓名成功')
    if select_num==2:
            if len(member_list):
                for x in range(0,len(member_list)):
                    print(x+1,member_list[x])
            student_num=int(input('请输入修改的姓名'))
            while student_num<0  or  student_num>len(member_list):
                student_num=int(input('输入序号错误,请重新输入序号'))
                new_name=input('请输入要修改的姓名')
                member_list[student_num-1]=new_name
            print('学员信息修改完成')
    else:
            print('学员信息为空,无法修改')
    if select_num==3:
            if len(member_list):
                for x in range(0,len(member_list)):
                    print('''1-输入序号查询
                    2-查询所有学员
                    ''')
            select_num=int(input('请输入操作序号'))
            while select_num!=1 or select_num!=2:
                select_num=int(input('输入操作序号错误,请重新输入:'))
                if select_num==1:
                    student_num=int(input('请输入学员序号'))
                while student_num<0 or student_num>len(member_list):
                     student_num=int(input('输入序号错误,请重新输入正确序号'))
                     name=member_list[student_num-1]
                     print('查询到的姓名是%s'%(name))
            else:
                print('学员信息为空,无法查询')
    if select_num==4:
        if len(member_list):
            print('''
            1-输入序号删除
            2-输入名字删除
            3-删除所有学员
            ''')
        for x in range (0,len(member_list)):
            print(x+1,member_list[x])
        select_num=int(input('输入操作序号'))
        while select_num<1 or select_num>3:
            select_num=int(input('输入错误,重输'))
        if select_num==1:
            if select_num == 1:
                select = int(input('请输入要删除的学员序号：'))
                while select < 1 or select > len(member_list):
                    select = int(input('编号不存在,请重新输入要删除的学员序号：'))
                member_list.pop(select - 1)
                print('删除学员成功！')
            if select_num == 2:
                name = input('请输入要删除的学员名称:')
                while name not in member_list:
                    name = input('请重新输入要删除的学员姓名:')
                member_list.remove(name)
                print('学员信息删除成功！')
            if select_num == 3:
                while len(member_list):
                    del member_list[0]
                print('学员信息删除成功')
            else:
                print('学员信息为空，无法删除！')

    if select_num == 0:
                break

"""
座右铭:将来的你一定会感激现在拼命的自己
@project:7-20
@author:Mr.Zhang
@file:手机通讯录系统.PY
@ide:PyCharm
@time:2018-07-20 09:04:39
"""
list_student=['郝超杰','李威','李四','张广师','李宇恒','池永伟','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪']
#声明一个空字典
#{'郝':[郝超杰,郝人，郝建]}
student_dict={}
#遍历联系人列表，把每个人的姓氏取出来
for student in list_student:
    #第一人：郝超杰
    #第二个人：李威
    #第三个人：李四
    #把每个人的姓氏从姓名这个字符串中取出来。
    first_char=student[0]

    #姓氏：郝
    #姓氏：李
    #姓氏：李
    #判断姓氏是否在字典当中
    if first_char in student_dict:
        #如果有姓氏这个键，则把对应的联系人列表取出来
        #[李威]
        result_list=student_dict[first_char]

        #再把同样姓氏的这个人，给放到联系人列表当中。
        result_list.append(student)
        #[李威，李四]

    else:
        #如果字典中没有姓氏这个键，则把对应的联系人存放在列表当中。
        #[郝超杰]
        #[李威]
        result_list=[student]


        student_dict[first_char]=result_list
        #student_dict={'郝':[郝超杰],'李'：[李威]}


while True:
    print('''
    1-查询
    2-退出
    ''')

    select_num=int(input('请选择操作的序号:'))
    while select_num!=1 and select_num!=2:
        select_num=int(input('输入错误，请重新输入:'))
    #如果用户选择序号1，用户要查询联系人
    if select_num==1:
        select_char=input('请输入您要查询的姓氏:')
        #判断输入的姓氏在不在字典当中
        if select_char in student_dict:
            #如果姓氏在字典当中，则以输入的姓氏为键取出对应的联系人列表，然后对联系人列表进行遍历
            stu_list=student_dict[select_char]
            for index,value in enumerate(stu_list):
                print(index+1,'-',value)
        #如果姓氏不在字典当中
        else:
            print('查无此人！')
    elif select_num==2:
        break













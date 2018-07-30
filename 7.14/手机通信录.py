list_student=['郝超杰','郝人','吕朝朝','张广师','李宇恒','池永伟','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪']
#声明一个空字典
student_dict={}
for student in list_student:
    first_char=student[0]
    if first_char in student_dict:
        student_list=student_dict[first_char]
        student_list.append(student)
    else:
        student_list=[student]
        student_dict[first_char]=student_list
while True:
     print('''
     1-查询
     2-退出
     ''')
     select_num=int(input('请输入操作序号:'))
     while select_num!=1 and select_num!=2:
         select_num=int(input('输入错误,请重新输入操作序号:'))
     if select_num==1:
         name_char=input('请输入姓氏:')
         if name_char in student_dict:
            stu_list=student_dict[name_char]
            for index, result in enumerate (stu_list):
                print(index+1,result)
         else:
             print('查无此人')
     else:
         break





list_student=['郝超杰','李威','吕朝朝','张广师','李宇恒','池胖子','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪']     #定义列表
student_dict={} #声明一个空字典
for student in list_student:#a遍历所有联系人
# 从每个人的名字中取出姓氏,联系人的人的分类就是以姓氏为键
   fist_char=student[0]
   # 判断字典中是否已经存在fist_char这个键
   if fist_char in student_dict:
       #如果有这个键,通过键取出联系人列表
       result_list=student_dict[fist_char]
       #res_list:['郝超杰','好人']
       result_list.append(student)

   else:
       # 如果没有这个键
       #创建这个键,并且给这个件配置一个联系人列表
    result_list=[student]
    student_dict[fist_char]=result_list

while True:
    print('''
    1-查询
    2-退出
    ''')
    select_number=int(input('请选择操作序号'))
    while select_number !=1 and  select_number!=2:
        select_number=int(input('输入错误,请重新输入'))
    if select_number==1:
        select_char=(input('请输入查询联系人姓氏'))
        #判断输入联系人姓氏在不在字典当中
        if select_char in  student_dict:
            #如果在,则已输入的姓氏为键取出对应值,然后遍历联系人
              stu_list=student_dict[select_char]
              for index , result in enumerate(stu_list):
                  print(index+1,'-',result)
    if select_number==2:
        break






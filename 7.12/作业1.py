
list_student=['郝超杰','李威','吕朝朝','张广师','李宇恒','池永伟','黄保安','陈鹏','余江帆','曹森','郑慧诏','郭克松','高翔','杨建宇','孟新珂','司金辉','张梦冉','王坤峰','蔡飞','樊俊','张稼瑞','吴亚涛','葛成云','王鹏基','樊俊峰','张崇雷','陈泽坤','王震宇','曾一飞','凌晨洋','郑雪鹏','李鑫一','晋吉祥','王晓茹','陶林','范雪婷','岳银龙','王继涛','张力方','牛铭瑞','马深凌','楚少杰','刘家豪']     #定义列表
name_dict={}  # 定义一个空字典
for  name in list_student:  #   输入名字在list中
     fist_char = name[0]  #姓氏 ,用作键
    if fist_char in name_dict.keys():
        list1 = name_dict[fist_char]

           list1.append(name)
        print(list1)
       #用于生成字典

      else:
           name_dict[fist_char] = [name]  #如果字典中无名字则加入字典
while True:
     s = input('请输入要查找的联系人姓氏：')
     if s in name_dict.keys():
         list1 = name_dict[s]
                                #在字典中查询键s 并把键值对输出给list1列表
         for index, name in enumerate(list1):
             print('序号：%s，姓名：%s' % (index+1, name))  #遍历查询字典
     else:
       print('没有找到联系人')      #通过查询字典找到姓名
     # coding:utf-8
 lis=[]
 for line in f:
     print(line)
     res=line.split('"')
     print(res)
 for x in res :
  if x[0]=='h':
   lis.append(x)
 print(lis)
 f=open('字符串方法练习.txt','r',encoding='utf-8')
 list=[ ]
 for line in  f:
     res=line.split('"')
 for x in res:
     if x[0]=='h':
      list.append(x)
 print(list)
 f.close
 f.read(10)
 print(f.read(10))
 f_new=open('字符串方法练习.bak','w',encoding='utf-8')
 for line in f:
      if '所有网址'in line :
          line=line.replace('所有网址','7777')
          f_new.write(line)
      else:
          f_new.write(line)
f.close()
 f_new.close()
#
#
#
#
#
#

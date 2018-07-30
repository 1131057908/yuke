man_age=int(input('请输入男生年纪:'))
man_height=int(input('请输入男生身高:'))
man_weight=int(input('请输入男生体重:'))
man_income=int(input('请输入男生收入:'))

woman_age=int(input('请输入女生年龄 '))
woman_height=int(input('请输入女生身高'))
woman_weight=int(input('请输入女生体重'))
woman_income=int(input('请输入女生收入'))

if (20<=woman_age<=25) and (160<=woman_height<170) and (45<=woman_weight<=60)and (woman_income>=2000):
  if (20<man_age<25) and (170<man_height<180) and (65<man_weight<85) and (man_income>6000):
    print('何时约会')
  else:
     print('男生不符合要求')
else:
    print('女生不符合要求')
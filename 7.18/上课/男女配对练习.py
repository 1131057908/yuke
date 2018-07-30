man_age=int(input())
man_height=int(input())
man_weight=int(input())
man_income=int(input())



woman_age=int(input())
woman_height=int(input())
woman_weight=int(input())
woman_income=int(input())



if(20<=woman_age<=30) and (150<=woman_height<=170) and (50<=woman_weight<=60) and (woman_income>2000):
  if (man_age<=25) and (man_height>175) and (60<man_weight<80) and(man_income>10000):
   print('老弟合适')
  else:
   print('你是好人')
else:
  print('没看中')
"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:文件的修改.PY
@ide:PyCharm
@time:2018-07-20 14:41:51
"""


f=open('ThatGirl.txt','r',encoding='utf-8')
#已写入的方式打开文件，如果文件不存在直接创建
f_new=open('ThatGirl.bak','w',encoding='utf-8')
for line in f:
      if '别让他错过' in line:
          line=line.replace('别让他错过','错过就错过')
          f_new.write(line)
      else:
          f_new.write(line)
f.close()
f_new.close()





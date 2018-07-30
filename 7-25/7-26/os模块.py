"""
座右铭:吃饱不饿，努力学习
@project:7-26
@author:Mr.Huang
@file:os模块.PY
@ide:PyCharm
@time:2018-07-26 09:27:16
"""

#os 全称是(oprationaSystem)操作系统
#os:用于操作文件/文件夹等等
import os
#1.cpu_count()
# count=os.cpu_count()
# print('cpu的个数:',count)
#根据cpu个数可以决定创建几个进程更合适,cpu个数=最好的进程数



#2.*******************************getcwd():返回当前文件夹的绝对路径********
# cwd=os.getcwd()
# print('当前项目的绝对路径{}'.format(cwd))



#3.name:系统名称
# nt:windows系统
# name=os.name
# print('操作系统的 名称:',name)


#4.os.path.abspath():返回自身所在路径的绝对路径
# result=os.path.abspath('os模块.py')
# print('绝对路径{}'.format(result))



#5.os.path.basename:取路径最后一部分
# result_1=os.path.basename('C:/Users/Administrator/Desktop/7-26/os模块.py')
# print('取路径的最后一部分{}'.format(result_1))


#6.os.path.dirname():返回当前文件/文件夹所在的父级文件夹
# result_2=os.path.dirname('C:/Users/Administrator/Desktop/7-26/os模块.py')
# print('当前文件所在上一级目录{}'.format(result_2))


#7.************** os.path.exists()判断路径下的文件是否\存在  返回true存在  false不存在
# result_3=os.path.exists('C:/Users/Administrator/Desktop/7-26/os模块.py')
# print(result_3)



#8. os.path.isfile():判断是否为文件
# result_4=os.path.isfile('os模块.py')
# print('是不是一个文件{}'.format(result_4))

# 9.os.path.isdir();判断是否为文件夹
# result_5=os.path.isdir('C:/Users/Administrator/Desktop/7-26/os模块.py')
# print('是否为文件夹{}'.format(result_5))

# 10.**9******************************os.path.join():拼接路径
# result_6=os.path.join('C:/Users/Administrator/Desktop/7-26/','os模块.py')
# print('拼接路径{}'.format(result_6))
#11.****************************** mkdir()创建文件
#如果在dir_1继续创建文件夹需要切换dir_1这个文件夹
# os.mkdir('dir_1')
# print(os.getcwd())
#12.****************************chidr()切换文件夹
# os.chdir('dir_1')
# os.mkdir('dir_4')

# os.mkdir('dir_2')
# os.mkdir('dir_3')
# print(os.getcwd())
#13.makedirs  递归创建出文件夹,exist_ok,已经存在也不报错
# os.chdir('7-26')
os.makedirs('a/b/c/d',exist_ok=True)
os.makedirs('1/2/3',exist_ok=True)
# #补充:递归更名
# os.renames('a/b/c/d','e/f/g/h')


# 14.removedirs:递归删除文件夹
# os.removedirs('a/b/c/d')
#mknod()  创建文件  but window上面的python不支持这样创建

# os.mknod('test.txt')

#16.****************************************rename():文件更名.
# os.rename('test','test1.txt')


# #************************************************17.remove;文件删除
# os.remove('tt1.txt')
#


#18************************************************** os.path.pardir:返回当前文件或文件夹所在的父集目录
#..父级目录
#.当前目录
#cudir()当前目录
# print('当前文件/文件夹所在父级目录;{}'.format(os.path.pardir))





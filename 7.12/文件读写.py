#Author:zhang
#大象装进冰箱三个步骤：1.打开冰箱 2.把大象塞进去 3.关闭冰箱门
#文件读写三个步骤：1.打开文件 2.读/写 3.关闭文件

#文件打开模式：
#r：只读模式
#w：只写模式
#a：追加写入模式
#w+:写读模式，能写也能读，也是覆盖写入，但是写入数据的位置会根据光标的位置而定
#r+：读写模式，能写也能读。默认也是覆盖写入。
#a+：追加读写,能写能读，写入的数据会追加到原数据的最后。
#rb：二进制读，但是不能设置编码，因为默认就是二进制格式。
#rw：二进制写，但是需要更改写入文件的编码格式。
#ab：二进制追加模式。


#1.创建文件操作的句柄
#open():第一个参数：文件名 第二个参数：文件的打开方式，第三个参数：编码格式,参数之间的位置不能调换。
#

# #tell()：显示光标的位置
# print(f.tell())
# #read()：读文件，括号里可填写读取字符的个数。如果不填参数，默认读取文件的全部内容。
# print(f.read(10))
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.read(3))
#文件在读取的模式下，是不能写入数据的。文件在写入的模式下,也无法读取数据。
# f.write('haha')
# print(f.read())
# print(f.tell())
#f.encoding：文件的编码格式
# print(f.encoding)
#f.name:文件的名称
# print(f.name)

# f=open('ThatGirl.txt','a',encoding='utf-8')
# # print(f.read(5))
# #'w'：写入模式，写进去的数据会覆盖原有数据。
# f.write('Hello')

# f=open('ThatGirl.txt','r',encoding='utf-8')
#readline()：一次只读取一行数据
# print(f.readline())
# print(f.readline())
# print(f.readline())
#readlines()：会读取所有行的数据，但是会将每一行的数据当成一个元素存放在列表当中。
# print(f.readlines())
# print(f.truncate(3))

# f=open('ThatGirl.txt','w+',encoding='utf-8')
# f.write('Hello')
# print(f.read())

# f=open('ThatGirl.txt','r+',encoding='utf-8')
# print(f.read(3))
# f.write('哈哈哈')

# f=open('ThatGirl.txt','r+',encoding='utf-8')
# # f.write('world')
# # print(f.read(5))
# f.write('哈哈哈呵呵呵嘿嘿嘿')

f=open('test.txt','w+',encoding='utf-8')

f.write('111')
f.seek(2)
print(f.read())



#字符串也可以理解为一个容器，他也是有序的 也存在索引值，字符串
#---------字符串常用函数-----------
string='下午好'
#1.len(string)
res1=len(string)
print(res1)
#2.字符串的取值
res2=string[0]
print(res2)
#3.切片查询
res3=string[0:2]
print(res3)
#倒叙查询
res4=string[-1]
print(res4)
#3.count():统计某个字符出现的次数
res5=string.count('下')
print(res5)
#4.find()用于查询某字符在字符串中出现的索引位置，会直接返回该字符所在位置的起始位置，不存在该字符返回-1
#find()参数1：要找的字符串，第二参数：找的开始位置，参数3：找的结束位置，（取头不取尾）
find_str='午'
res6=string.find(find_str,0,1)
print(res6,'----')


find_str_1='下午'
res7=string.find(find_str_1)
print(res7)

#index():在匹配到合适的字符后会直接返回该字符所在位置的起始索引值



#upper（）小写转成大写

#lower（）将大写改为小写




#strip()去除字符串首尾两端指定字符，括号中填写要去楚字符



#split():根据指定字符对一个字符串进行分割。返回值是一个list列表



#replace：使用新字符替换旧字符
# 括号里第一参数是旧字符 第二参数 是新字符



# startwith；判断一个字符是否是以某一字符开头，返回结果是true huozfalse


#endwith ：判断某一字符串是否是以某一字符开头 返回结果 true  false
#不可通过索引


#-------------------字符串的添加修改----------、
#通过索引查询

# #修改
# string  转换成 list

0
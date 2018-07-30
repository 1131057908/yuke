# 字符串也可以理解为一个容器,也存在索引值
# ----------------------------字符串常用函数-------------
string='德玛西亚'
# len();获取字符串长度
res1=len(string)
print(res1)
# 字符串根据索引值取值
res2=string[0]
print(res2)
# 切片查询
res3=string[0:2:1]
print(res3)
res20=string[::2]
print(res20,'huihas')
# 倒序查询
res4=string[-1]
print(res4)
# revers()

# count:统计字符出现的次数
res5=string.count('德')
print(res5)
# find()  在匹配到合适的字符串之后,会直接返回字符串所在位置的起始索引值,默认返回识别第一个匹配值
# 可在后面设置查询范围,如果查询不到合适的字符串,会返回-1
find_str='西亚'
res6=string.find(find_str)
print(res6,'bbbbbbbbbbb')
res7=string.find(find_str,0,1)
print(res7)
# index():在匹配到合适的字符串之后,会直接返回该字符转的起始位置的起始索引值
# 如果没有查询到合适的字符串会报错
res8=string.index(find_str)
print(res8)
# res9=string.index(find_str,0,1)
# print(res9)


# upper()将小写字母,全部转为大写
string='abcd'
res10=string.upper()
print(res10)
# lower():将大写英文字母,全部转换为小写
string2='EDG'
res11=string2.lower()
print(res11)
# stip():去除字符串首尾两端的指定字符
string3=';abcd'
res12=string.strip(';')
print(res12)
# split():根据指定字符对一个字符串进行分割,返回值是一个list列表
string13='a;b;c;d'
res13=string.split(';')
print(res13)
# replace(0;使用新的字符串替换旧的字符串)
string5='abc'
res14=string5.replace('b','-')
print(res14,'啊啊啊啊' )
# startwith();判断一个字符串是否易某一个字符开头  返回结果是true 或者false
string6='abcd'
res15=string6.startswith('a')
print(res15)
# endwith();判断一个字符串是否以某一个字符结尾,返回结果是true 或者false
res17=string.endswith('d')
print(res17)
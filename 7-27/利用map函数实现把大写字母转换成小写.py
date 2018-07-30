"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:利用map函数实现把大写字母转换成小写.PY
@ide:PyCharm
@time:2018-07-27 09:56:17
"""
def char_lower(string):
#将字符串全部转换成小写字母
     all_char_dict={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l'}
#声明一个变量,记录最终转换结果,
     result=''
#遍历string这个字符串,将其大写字母转换成小写
     for char_str in string:
         if char_str.isupper():
          #l如果从string取出大写则从字典取出小写,如果从string是小写,直接取出
             every_char_result=all_char_dict[char_str]
         else:
             every_char_result=char_str
         result+=every_char_result
     return result
res=char_lower('AdDc')
print(res)
res1=list(map(char_lower,['Auhd','Dcrjk']))
print(res1)


def custom_lower(s):

    def char_lower(string):
    # 将字符串全部转换成小写字母
        all_char_dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l'}
    # 声明一个变量,记录最终转换结果,
        result = ''
    # 遍历string这个字符串,将其大写字母转换成小写
        for char_str in string:
            if char_str.isupper():
            # l如果从string取出大写则从字典取出小写,如果从string是小写,直接取出
                every_char_result = all_char_dict[char_str]
            else:
                every_char_result = char_str
            result += every_char_result
        return result
    if isinstance(s,list):#issubclass():#判断某一变量是否属于某一类型,如果是返回true 不是返回false
        return list(map(char_lower,s))
    else:
        return char_lower(s)
res1=custom_lower('kaAb')
print(res1)
res2=custom_lower(['adc'])
print(res2)
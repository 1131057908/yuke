# 拼接字符串:就是将不同字符串或变量拼接成一个完整的字符串内容
#
# 第一种:使用占位符拼接字符串
# %d:整数类型的占位符  % -'数字' d 增大间隔
age=20
score=100
result="小明的年龄是%d,成绩是%d"%(age,score)
print(result)
# 拼接字符串的时候,如果之拼接一个变量,那么%后面不需要添加().
# 拼接两个或两个以上的变量需要加()
height=180
result1='小刚的身高是%d'%height
print(result1)

# %f : 小数类型的占位符,用于拼接小数类型的变量
# 默认情况下取小数点后六位
# .数字f 就是取小数点后几位
weight=135.5
result2='小红的体重是%f'%weight
print(result2)
result3='小红的体重是%.1f'% weight
print(result3)
result4='小红的体重是%.2f' %weight
print(result4)
result5='小红的体重是%.8f'%weight
print(result5)



# %s 通用占位符 可以拼接任意类型数据
name='张三'
age=18
height=178.5
sex='male'
result6='他的名字是%s,年龄是%s,身高是%s,性别是%s'%(name,age,height,sex)
print(result6)

# 第二种:使用加号拼接,加号只能拼接字符串类型
result7='今'+'晚'+'吃'+'鸡'+'吗'
print(result7)
result8="大"+"吉"+"大"+"利"
print(result8)


# 第三种:使用.format()拼接
name='小白'
age=50
sex='famle'
weight=130.5
result9='他的姓名是{1},年龄是{3},性别是{0},体重是{2}'.format(name,age,sex,weight)
print(result9)
# 使用.format对字符串拼接的时候,小括号填写拼接的变量{}中设置变量顺序,顺序的编号默认从0开始
# 以此向后加1
# if 条件语句:
#     第一种:
#     if __name__ == '__main__':
#         if....if...
#     第二种: if ...else
#     第三种: if  elif
name='李四'
if name=='张三':
    print("姓名是张三")
if name=="李四":
    print("姓名是李四")
if name=="王二":
    print("姓名是王二")
 # "=="比较运算符用于比较左右两边的值是否相等.结果返回的true和false
 # Python对代码的锁紧要求严格 ,因为python是通过缩进判断代码之间的包含关系
 # 如果某行代码的缩进比前面代码的缩进多,说明该行代码是被包含关系.如果代码之间缩减一致,说明是同等级关系
age=20
if age==28:
    print("年龄是二十岁")
else:
    print('年龄不是二十岁')



animal='小鹿'
if animal=='小猫':
    print('这个动物是小猫')
elif animal=='小熊':
    print('这个动物是小熊')
elif animal=='小鹿':
    print('这个动物是小鹿')
elif animal=='小狗':
    print('这个动物是小狗')
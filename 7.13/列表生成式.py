# 列表生成式:快速生成列表的一种方式
# 特点;会将将所有结果计算出来存在列表中,这样会占用很大内出空间,如果列表中的数据比较多的时候比如10万
# 或者更高这样程序运行比较卡顿
my_list=[]
for x in range(1,11):
    res=x*x
    my_list.append(res)
    print(my_list)


fast_list=[ x*x for x in range(1,11)]
print(fast_list)
# if 判断
fast_list_1=[x*x for x in range (1,11) if x!=2]
print(fast_list_1)
# 遍历1-11 的数字,让数字奇数的结果进行相乘的运算 x*x
jishu_list=[x*x for x in range(1,11) if x %2==1]
print(jishu_list)
# 列表生成式支持双重for循环
res2=[x*y for x in range(1,4) for y in range (1,4)]
print(res2)
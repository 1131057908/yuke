#通过列表生成式,我们可以直接创建出来列表,但由于内存的限制,;列表的容量
# 也是有限加入一个列表的数据十分庞大 ,而我们需要访问前面几个元素,那么就造成后面大多数元素占用的内存空间被白白浪费
fast_list=[x*x for x in range (0,100000000)]
print(fast_list)
fast_list=(x*y for x in range (1,4) for y in range(1,4))
# print(fast_list)
# 列表生成器;并不会一次性将所有计算结果存放在内存中,而是在使用某一些值得时候才会去计算结果并返回,而没有使用的值不会计算
#
# 在使用next()方法从列表生成器取值的时候,如果元素被取完接着去会报错'  stopinterration' \
fast_list=(x*x for x in range(0,2))
print(fast_list)
print(next(fast_list))
print(next(fast_list))
print(next(fast_list))
for x in fast_list:
    print(x)

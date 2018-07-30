# 将字符串"k:1|k1:2|k2:3|k3:4"处理成Python字典{k:1,k1:2,k2:3,k3:4}

# string="k:1|k1:2|k2:3|k3:4"
# list1=string.split('|')
# print(list1)
# dict1={}
# for x in list1:
#     # print(x)
#     list2=x.split(':')
#     print(list2)
#     dict1[list2[0]]=int(list2[1])
# print(dict1)
# string = "k:1|k1:2|k2:3|k3:4"
# list2=list(string.split('0:3'))
# list2=list(string.split('9:13'))
# list3=list(string.split('9:13'))
# list4=list(string.split('14:18'))
# # res1=string.replace('')
# for x in string:
#     str1=string.split('|')
#     # str2=str1.split(':')
# print(str1)
# dict1={}
# for x in str1:
#     print(x)
#     res=x.join(x)
# str2=x.remove(':')
# print(str2)
# dict1[str2[0]]=int(str2[1])
# print(dict1)



# print(list2)
#
# string="k:1|k1:2|k2:3|k3:4"
# list1=string.split('|')
# print(list1)
# dict1={}
# for x in list1:
#     # print(x)
#     list2=x.split(':')
#     print(list2)
#     dict1[list2[0]]=int(list2[1])
# print(dict1)



#
# string1 = 'k:1|k1:2|k2:3|k3:4'
# res1 = string1.replace('|',':')
# print(res1,type(res1))
# res2 = res1.split(':')
#
# print(type(res2),res2)
# dict1 ={}
# for x in range(0,len(res2)):
#     print(x)
#     if x%2==0:
#         dict1[res2[x]] = int(res2[x+1])
# print(dict1)
# #
# string="k:1|k1:2|k2:3|k3:4"
# res1=string.replace('|',':')
# res2=res1.split(':')
# dict1={}
# for x  in range(0,len(res2)):
#     if x %2==0:
#        dict1[res2[0]]=int(res2[x+1])
# print(dict1)

# # """
# # 座右铭:吃饱不饿，努力学习
# # @project:预科
# # @author:Mr.Huang
# # @file:练习map,reduce.PY
# # @ide:PyCharm
# # @time:2018-07-27 11:11:06
# # """
# # from functools import reduce
# #
# #
# # def char_to_number(string):
# #     all_number_dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# #     return all_number_dict[string]
# # res=list(map(char_to_number,'123'))
# # print(res)
# # def result_number(x,y):
# #     res=x*10+y
# #     return res
# # result=reduce(result_number,res)
# # print('最终结果:',result,'最终类型',type(result))
# # def TNT(s):
# #     def char_to_number(string):
# #         all_number_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# #         return all_number_dict[string]
# #     def result_number(x,y):
# #         res=x*10+y
# #         return res
# #     return reduce(result_number,map(char_to_number,s))
#
#
# #-------------------转换大小写********************
#
#
# def char_lower(string):
#     all_char_dict = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
#                      'K': 'k', 'L': 'l'}
#     # 声明一个变量,记录最终转换结
#     result=''
#     for char_str in string:
#         if char_str.isupper():
#             every_char_result=all_char_dict[char_str]
#         else:
#             every_char_result=char_str
#         result+=every_char_result
#     return result
# wewwswwwwwwww31res=list(map(char_lower,['abcD,abCd']))
# res1=char_lower('AAAA')
# print(res)
#



# def  calc(list1):
#     for  x  in list1:
#         res=x*x
#         # return  res
#         print(res)
# calc([1,2,3,4])



# def  calc(x):
# 	res=x*x
# 	return res
# result=map(calc,[1,2,3,4])
# print(result)
# for y in result:
#    print(y)
# list2=[]
# def  str_int(str):
#     for x in str:
#         li=int(x)
#         list2.append(li)
#     print(list2)
# str_int(('1','2','3'))
# list1=[]
list2=[]
result1=map(str,[1,2,3,4,5,6])
print(result1)
for  x in result1:

    list2.append(x)
print(list2)


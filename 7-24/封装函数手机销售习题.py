"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:封装函数手机销售习题.PY
@ide:PyCharm
@time:2018-07-24 20:48:29
"""


phone_info = [{'name':'vivox9', 'price':'1200', 'count':'30'},
{'name':'iphone6', 'price':'2000', 'count':'55'},
{'name':'iphone6s', 'price':'2200', 'count':'120'},
{'name':'iphone7', 'price':'4000', 'count':'80'},
{'name':'iphone7s', 'price':'4200', 'count':'90'},
 {'name':'iphone8', 'price':'5200', 'count':'70'}]

#查看所有品牌的函数
def  select_all_phone(is_detail):
    for x in range(0,len(phone_info)):
        phone_dict=phone_info[x]

        if is_detail==True:
           print('{}.品牌{},价格{},库存{}'.format(x+1,phone_dict['name'],phone_dict['price'],phone_dict['count']))
        else:
           print('{}.品牌{}'.format(x+1,phone_dict['name']))









#定义查看某个产品的详细信息 或返回一个函数

def detail_info_or_back():
    print('''
    1-根据产品序号查看手机详细信息
    2-返回
    ''')
    #根据控制台输入的数字,来进行哪项判断
    select_opration=int(input('请输入你要操作的序号;'))
    while select_opration!=1 and select_opration!=2:
        select_opration=int(input('输入操作序号错误,请您重新输入:'))
    if select_opration==1:
        select_all_phone(False)
        select_number=int(input('请您输入选择的手机序号:'))
        while select_number not in range (0,len(phone_info)):
            select_number=int(input('输入序号错误,请重新输入:'))
        phone_dict=phone_info[select_number-1]
        print('{}.品牌{},价格{},库存{}'.format(select_number,phone_dict['name'],phone_dict['price'],phone_dict['count']))
        buy_or_back(phone_dict)


    else:
        return













#定义一个购买或者返回的函数，设置一个参数接受某个手机的字典信息

def buy_or_back(phone_dict):
    print('''
    1-购买
    2-返回
    ''')
    select_number=int(input('请您输入操作序号:'))
    while select_number!=1  and select_number!=2:
        select_number=int(input('输入序号错误,请您重新输入:'))
    if select_number==1:
        total_count=int(phone_dict['count'])
        print('当前库存为%s'%total_count)
        buy_count=int(input('请您输入购买数量:'))
        while buy_count <= 0 or buy_count > total_count:
            buy_count=int(input('请您重新输入购买数量:'))
    #根据购买数量计算剩余库存,修改原有库存数量
        shengyukucun_count=total_count-buy_count
        phone_dict['count']=str(shengyukucun_count)
        if int(phone_dict['count'])==0:
            phone_info.remove(phone_dict)
        print('购买成功')
    else:
        return

















#定义添加产品或者修改产品的函数
def  add_or_uodate_phone_info():
        print('''
        1-添加新产品
        2-修改原有产品
        ''')
        select_number = int(input('请输入要选择的序号:'))
        while select_number != 1 and select_number != 2:
            select_number = int(input('输入错误，请重新输入要选择的序号：'))
        if select_number==1:
            new_name=input('请输入新产品名称:')
            new_price = input('请输入新产品价格:')
            new_count = input('请输入新产品库存:')
            new_phone_dict={'name':new_name,'price':new_price,'count':new_count}
            phone_info.append(new_phone_dict)
        else:
            #调用select_all-phone函数,参数设置为True,根据编号修改数据
            select_all_phone(True)
            print('1-根据产品序号修改产品信息')
            print('2-返回')
            select_number = int(input('请输入你要操作的序号:'))
            while select_number != 1 and select_number != 2:
                select_number = int(input('输入的序号有误，请重新输入要操作的序号:'))
            # 如果用户选择序号1，则根据产品序号修改产品信息
            if select_number == 1:
                phone_num = int(input('请输入要修改的手机序号:'))
                while phone_num < 1 or phone_num > len(phone_info):
                    phone_num = int(input('手机输入错误，请重新输入要修改的手机序号:'))
                update_dict=phone_info[phone_num-1]
                update_name=input('请输入修改的名称:')
                update_price=input('请输入修改的价格:')
                update_count=input('请输入修改的库存:')
                update_dict['name'] = update_name
                update_dict['price'] = update_price
                update_dict['count'] = update_count
                print('修改成功')
            else:
                return















#定义一个删除或者返回函数
def delete_phone_or_back():
    print('1-根据序号删除产品')
    print('2-删除所有产品')
    print('3-返回')
    select_number = int(input('请输入要操作的编号:'))
    while select_number != 1 and select_number != 2 and select_number != 3:
        select_number = int(input('输入错误，请重新输入要操作的编号:'))
    # 用户选择1，要根据产品序号删除。
    if select_number == 1:
        select_all_phone(True)
        number = int(input('请选择要删除的产品编号:'))
        while number < 1 or number > len(phone_info):
            number = int(input('输入错误，请重新选择要删除的产品编号:'))

        del phone_info[number-1]
    elif select_number==3:
        return













#----------------------------------主函数----------------------------------
while True:
    print('''
    欢迎使用手机销售系统
    1--查看所有手机品牌
    2--添加或者修改手机信息
    3-删除手机信息
    4-退出程序
    ''')
    select_number=int(input('请输入操作序号：'))
    while select_number not in range (1,5):
        select_number=int(input('输入序号错误，请重新输入：'))
    if select_number==1:
        if len(phone_info):
            detail_info_or_back()
        else:
            break
    elif select_number==2:
        add_or_uodate_phone_info()
    elif select_number==3:
        delete_phone_or_back()
    elif select_number==4:
        break
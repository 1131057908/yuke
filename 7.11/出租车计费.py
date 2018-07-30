

while True:
    km=int(input('请输入公里数'))
    if km<0:
        print('输入公里数错误,请重新输入')
    if 0<=km<=2:
        print('您需花费8元')
        break
    if 2<km<=12:
        cost=(km-2)*12+8
        print('您需花费%s'%cost)
    if km>12:
        cost=(km-12)*1.5+(12-2)*1.2+8
        print('您需花费:%s'%cost)
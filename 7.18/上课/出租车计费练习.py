while True:
    km=int(input('请输入公里数：'))
    while km<0:
        km=int(input('输入错误，请重新输入：'))
        break
    if 0<km<=2:
      cost=8
      print('您需支付%s'%cost)
    elif 2<km<=12:
        cost=8+(km-2)*1.2
        print('您需支付%s'%cost)
    elif km>12:
        cost=8+(12-2)*1.2+(km-12)*1.5
        print('您需要支付{}'.format(cost))
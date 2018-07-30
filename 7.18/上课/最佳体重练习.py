#最佳体重


while True:
    height=int(input('请输入您的身高：'))
    weight=int(input('请输入您的体重：'))
    while height<=0 or weight <=0:
        height=int(input('输入错误请重新输入体重：'))
        weight-int(input('输入错误请重新输入身高：'))
    best_weight=height-105
    if weight>best_weight:
        print('偏胖')
    elif weight<best_weight:
        print('偏瘦')
    elif weight==best_weight:
        print('完美')
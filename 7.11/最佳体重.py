while True:
    height=int(input('请输入身高'))
    weight=int(input('请输入体重'))
    best_weight=height-105
    if weight>best_weight:
        print('偏胖')
    if weight<best_weight:
        print('偏瘦')
    if weight==best_weight:
        print('体重正常')

while True:
    score=int(input('请输入您的成绩：'))
    while score not in range(0,101):
        score=int(input('输入错误，请重新输入：'))
    if score in range (0,60):
        print('不及格')
    if score in range(60,70):
        print('等级是D')
    if score in range(70,80):
        print('等级是C')
    if score  in range (80,90):
        print('等级是B')
    if score in range (90,101):
        print('等级是A')
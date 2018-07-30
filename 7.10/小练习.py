# 使用for循环实现九九乘法表

# 最外层for循环取值1-9
for x in range(1, 10):
    for y in range(1,x+1):
#   # x=1 for y in  range(1,2)y=1
#   # x=2 for y in range (1,3) y= 1,2
#   # x=3 for y  in range (1,4) y=1,2,3
#   #   x=4 for y  in range (1,5) y=1,2,3,4
# # print()语句默认有换行符,所有使用end=''替换掉换行符
        print('%d*%d=%d'%(y,x,x*y),end='  ')
    print('')
# 猜数字
import random
# random python中随机模块
# 首先生成一个随机整数
random_number=random.randint(0,1)
# 作弊手段
print('随机数:',random_number)
error_cout=0
while True:
    input_number=int(input('请输入要猜数字(0-10):'))

    while input_number<0 or input_number>2:
        input_number=int(input('输入的数字不在范围之内,请重新输入:'))
    if input_number>random_number:
        print('不好意思,数字猜大了')
    if input_number<random_number:
        print('不好意思,数字猜小了')
        error_cout+=1
    if input_number==random_number:
        print('''恭喜你猜对了
        1-继续猜
        2-退出
        ''')
        # error_cout=0
        select_number=int (input('请您选择操作序号:'))
        while select_number<1 or select_number>2:
              select_number=int(input('您选择的操作序号错误,请重新选择'))
        if select_number==1:
                random_number=random.randint(0,10)
        else:
                break
    if error_cout>=3:
        print('错误次数以达到三次,不给机会')
        break



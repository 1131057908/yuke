"""
座右铭:吃饱不饿，努力学习
@project:预科
@author:Mr.Huang
@file:心形.PY
@ide:PyCharm
@time:2018-07-21 16:09:34
"""


print('\n'.join([''.join([('❤'[(x - y) % len('❤')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
        x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

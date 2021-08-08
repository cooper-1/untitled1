# -*-coding:  UTF-8
# @Time    :  2021/7/18 16:40
# @Author  :  Cooper
# @FileName:  test1.py
# @Software:  PyCharm
url = '//car2.autoimg.cn/cardfs/product/g24/M09/C7/42/480x360_0_q95_c42_autohomecar__Chtk3WDDexOAbbz6ACB4viZsOBY625.jpg'
print(url[url.rfind('.'):])
print(url.rfind('.'))


def add(x, y):
    return x + y


def sub(x: int, y: int):
    '''
    :param x: 被减数
    :param y: 减数
    :return: 减法结果
    '''
    return x - y


x, y = 3, 2.5
print(sub(x, y) if x > y else add(x, y))
sub(5, 6)
print(15%2)

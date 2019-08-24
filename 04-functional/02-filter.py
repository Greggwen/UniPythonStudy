#!/bin/python3
"""
filter: Python 内置函数，用于过滤序列
filter() 接收一个函数和一个序列，filter会将传入的函数作用于序列的每个元素，然后根据返回值是True还是False决定保留还是丢弃
"""

# 给定一个list，只留下偶数，去除奇数
L = [1, 2, 3, 4, 8, 10, 23, 18]

def odd (ele):
    if ele % 2 == 0:
        return True 
    else:
        return False

FL = filter(odd, L)
print(list(FL))
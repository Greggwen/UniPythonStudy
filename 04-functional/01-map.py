#!/bin/python3

from functools import reduce

"""
map: map(f, iterA, iterB, ...) 返回一个遍历序列的迭代器
"""

# 例如
l = [1, 2, 3, 4, 5, 6]

def f(x):
    return x * x

r = map(f, l)
print(list(r))

# map传入的第一个参数为函数对象，而返回的结果是一个iterator，Iterator是惰性序列，因此需要通过list()函数来把序列计算并返回

# 再比如
r1 = map(str, l)
print(list(r1))

"""
reduce : 把一个函数作用在一个序列上，这个函数必须接受两个参数，reduce把结果继续和序列下一个元素做累积计算。
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
# 比如序列求合

def add(x, y):
    return x + y

r = reduce(add, l)

print(r)

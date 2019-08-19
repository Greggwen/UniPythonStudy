#!/bin/python3

"""
列表生成式：List Comprehensions
"""

import os

# 求 1-10 的平方

# 循环迭代方式
L = []
for i in range(1, 11):
    L.append(i * i)

print(L)

# 列表生成式
[print(x * x, end=" ") for x in range(1, 11)]

print()
# 想获取平方数为偶数的结果
[print(x * x, end=" ") for x in range(1, 11) if x % 2 == 0]

# 使用两层循环
[print(m + n ) for m in 'ABC' for n in 'ZXY']

# 使用列表生成式列出当前目录的文件和目录

[print(d) for d in os.listdir('.')]

# 循环字典
d = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}

for k, v in d.items():
    print(k, v)

[print(k, v) for k, v in d.items()]
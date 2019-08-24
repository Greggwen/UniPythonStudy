#!/bin/python3

"""
sorted: Python 内置函数
"""

# 对list进行排序
L = [36, 5, -12, 9, -21]
print(sorted(L))

# 同时sorted也是一个高阶函数，它还可以接收一个key函数来实现自定义排序
# 按绝对值大小来排序
print(sorted(L, key=abs))

# 以上是对数字进行排序，下面看下对字符串的排序
SL = ['a', 'b', 'z', 'X', 'm', 'y', 'J', 'V', 'N', 'j']

print(sorted(SL))
# 默认情况下，对字符串排序，是按照ASCII的大小比较的

# 同样，传入key也可以实现忽略大小写排序
print(sorted(SL, key=str.lower))

# 上面的排序我们得到的结果都是顺序排序下来的，那么如何反向排序呢
# sorted() 函数还接收第三个参数reverse=True来实现反向排序

print(sorted(SL, key=str.lower, reverse=True))


# sorted 是一个高阶函数，用sorted()排序的关键在于 key的映射函数的实现
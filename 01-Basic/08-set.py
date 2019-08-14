#!/bin/python3

"""
set是一个无序的不重复元素序列。
可以使用{ }或set()函数来创建集合。需要注意的是：若要创建一个空的集合，则必须使用set()。这是因为，{}是用来创建空字典使用的。
"""

s = set([1, 2, 3, 4, 5, 6, 7, 1, 2, 3])
print(s)

# 通过add(key)增加集合中
s.add(100)
print(s)

# 使用 remove(key)来删除集合某元素
s.remove(5)
print(s)

# 删除不存在key会报错
# s.remove(101)
# print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1 & s2)

print(s1 | s2)

# list是可变对象， 而str则为不可变对象
l1 = [1, 4, 2, 6]
l1.sort()
print(l1)

a = "abc"
a.replace('a', 'A')
print(a)
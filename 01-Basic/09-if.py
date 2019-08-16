#!/bin/python3

# 流程控制语句 if / for / while

# if 语句
x = int(input("Please input an integer:"))
if x < 0: 
    x = 0 
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# for 语句
words = ['cat', 'window', 'defenestrate']
for i in words:
    print(i, len(i))

# Example 1
# for w in words:
#     if len(w) > 6:
#         words.insert(0, w)

# print("Example 1 is ", words)

# Example 2
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print("Example 2 is ", words)

"""
若是需要在循环内修改序列中的值，应该先拷贝一份副本。
Example 1在执行过程中会一直不断的往words插入数据。
Example 2首先会执行一个words的副本，
"""

# range 函数
for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(0, 10, 3):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])

# 直接打印range()结果
print(range(5))
print(list(range(5)))

# pass 语句表示什么也不做。
while True:
    pass
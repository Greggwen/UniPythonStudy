#!/bin/python3

# 取一个list或tuple的部分元素是非常常见的操作
n = ['Michael', 'Bob', 'Jim', 'Rolly', 'Tracy', 'Sarah']

# 获取前三个元素放入到一个新的列表里

# Method 1 
r = [n[0], n[1], n[2]]
print(r)

# 如果我想获取的元素个数不确定，Method 1 就做不到了。
# Method 2，将获取元素个数做为变量来看
r = []
index = 3
for i in range(index):
    r.append(n[i])

print(r)

# Method 3 使用切片
r = n[:3]  # 相当于n[0:3]，表示从索引0开始，到3截止，但是不包括3
print(r)

# 例如
r = n[1:3]
print(r) # 表示获取列表n，索引为1，2的元素

# 同时，切片索引也支持负数，例如 
r = n[-2:]  
print(r) # 表示倒数第二个元素到最后一个元素,\

# 需要记住的是， -1代表的是列表或元组最后一个元素

# 来个栗子。创建一个0-99的列表
L = list(range(100))
print(L)

# 获取前10个元素
L1 = L[:10]
print(L1)

# 获取第10-20个元素
L2 = L[10:20]
print(L2)

# 获取最后10个元素
L3 = L[-10:]
print(L3)

# 前十个数，每两个获取一个
L4 = L[:10:2]
print(L4)

# 所有数，每5个取一个
L5 = L[::5]
print(L5)

# 完全复制一个列表
L6 = L[:]
print(L6)

# 元组也可以使用切片操作，操作结果仍然是元组，例如
p = (1, 2, 3, 4, 5, 6)
print(p[3: 5])

# 同样，字符串也可以看作是一个list，使用切片操作以后，依然是字符串，例如
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[3:9])
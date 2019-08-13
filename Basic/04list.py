#!/bin/python3

"""
list： 是python 内置的一种数据类型。list是一种有序集合，可以随时添加或删除其中元素。
"""

# 定义一个空list
list1 = []
print(list1)

classmates = ['Michael', 'Bob', 'Jim']
print(classmates)

# 获取list元素个数
print(len(classmates))

print("classmates[0] is %s" % classmates[0])
print("classmates[1] is %s" % classmates[1])
print("classmates[2] is %s" % classmates[2])

# print("classmates[3] is %s" % classmates[3])

print("classmates[-1] is %s" % classmates[-1])
print("classmates[-2] is %s" % classmates[-2])
print("classmates[-3] is %s" % classmates[-3])

# print("classmates[-4] is %s" % classmates[-4])

# 追回
classmates.append("Adam")
print("classmates.appen('Adam') is ", classmates)

# 把元素插到指定位置 
classmates.insert(2, "Rolly")
print(classmates)

# 删除list最后一个元素
lastEle = classmates.pop()
print(classmates)
print(lastEle)

# 删除list指定元素
specialEle = classmates.pop(1)
print(classmates)
print(specialEle)

# 替换list某个元素
classmates[0] = "JJ"
print(classmates)

# list里的元素可以是不同的数据类型，当然也可以是list
l1 = ["Rolly", 23, True, [100, 98, 99]]
print(l1)
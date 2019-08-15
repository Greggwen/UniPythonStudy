#!/bin/python3

"""
built-in func： Python 里内置了很多函数，可以直接调用
Pytho built-in doc: https://docs.python.org/3/library/functions.html
"""

# 获取帮助使用help函数， 例如 help(abs)

# 求绝对值
a = abs(-190)
print("-190的绝对值是", a)

# abs只接收一个参数，否则会报错
# a = abs(1, 2)

# 常用的还包括，求最大值，最小值，平均值
max_value = max(1, 2, 3, 4, 5, 6, 7)
min_value = min(1, 2, 3, 4, 5, 6, 7)
print("max value is %d and min value is %d" % (max_value, min_value))

max_value = max([1, 2, 3, 4, 5, 6, 7, 8])
min_value = min([1, 2, 3, 4, 5, 6, 7, 8])
print("max value is %d and min value is %d" % (max_value, min_value))

# 数据类型转换
i = int("1235")
print(i)

i = int("1235a", 16)  # 十六进制转换
print(i)

i = int(12.82)
print(i)

s = str(1.23)
print(type(s))

print(bool(1))
print(bool(2))
print(bool(0))
print(bool(-3))

print(float(12))

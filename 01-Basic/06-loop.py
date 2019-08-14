#!/bin/python3

# 循环列表
classmates = ['Michael', 'Bob', 'Jim', 'Rolly']

for name in classmates:
    print(name)

# 通过索引迭代
for i in range(len(classmates)):
    print(i, classmates[i])

# 计算1 + 2 + 3 + ... + 99 + 100

sum = 0
for i in range(101):
    sum = sum + i 

print(sum)

rows = int(input('输入列数： '))
i = j = k = 1 #声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
#等腰直角三角形1
print("等腰直角三角形1")
for i in range(0, rows):
    for k in range(0, rows - i):
        print(" * ", end=''), #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print("\n")
#!/bin/python3

print('I\'m OK!')
print('__name__ print is ' + __name__)

# 多行
print('''
Hello Python3!
I Love Python!
Welcome use Python!
''')

print('''Hello Swenly!\n Bye Bye!
''')

print(r'''Hello Swenly!\n Bye Bye!
''')

print(3 > 2)

# Bool
print("True and False is ", str(True and False))
print("True or False is ", str(True or False))
print("Not False is ", str(not False))

# None
print(None)

# 整数
a = 110
print(a)
print(type(a))
a = 'what'
print(a)
print(type(a))

# 赋值
a = "ABC"
print('var a is ', a)
b = a
print('var b = a, the value of b is ', b)
a = "EFG"
print('b is ', b)

# 常量
PI = 3.1415926
print(PI)

# 计算
i = 10 / 3 
print('10 / 3 is ', i)
i = 10 + 3.33333
print('10 + 3.33333 is ', i)
#!/bin/python3

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888
# abs函数
def my_abs(x):
    if x >= 0:
        return x # 代表函数执行完毕
    else:
        return -x

print(my_abs(-3))

# 计算平方值
def my_power(x):
    return x * x

print(my_power(5))

# 扩展，若求立方， 四次方
def my_power2(x, n = 2): # n = 2 为默认参数
    result = 1
    while n >= 1:
       result = result * x
       n -= 1
    return result

print(my_power2(5, 3))

# 参数设置

def persion_info (name, age, sex = 'boy', city = 'Beijing'):
    print("My name is %s" % name)
    print("I'm %d years old!" % age)
    print("I'm a %s" % sex)
    print("I live in %s" % city)


persion_info('Rolly', 23, city="Shanghai")

# Python的参数必须指向不可变参数，否则会掉进坑里

def add_end (L = []):
    L.append("END")
    return L

print(add_end([1, 2, 3]))
print(add_end([2, 3, 4]))
print(add_end([2, 'A', 'Start']))

# 看下面例子
print(add_end()) # ['END']
print(add_end()) # ['END', 'END']
print(add_end()) # ['END', 'END', 'END']
print(add_end()) # ['END', 'END', 'END', 'END']

# 比较疑惑的是： 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

# 原因在于： Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 我们调整下上面的函数
def add_end2 (L = None):
    if L is None:
        L = []
    L.append("END")
    return L

print(add_end2()) # ['END']
print(add_end2()) # ['END']
print(add_end2()) # ['END']
print(add_end2()) # ['END']

# 可变参数
# 可以使用list或者tuple来实现多参数
def calc(numbers):

    for i in numbers:
        print(i)

calc([1, 2, 3, 4])

# 使用参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc2(*numbers):
    for i in numbers:
        print(i)

calc2(1, 2, 3, 4)
calc2([4, 5, 6])

# 如果我们要以list里传参数, 传递 *list1 表示把list1这个list的所有元素作为可变参数传递
list1 = [7, 8, 9]
calc2(*list1)

# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person (name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person("Rolly", "25")
person("Rolly", 25, city="Beijing")

extra = {'city': 'Beijing', 'job': 'Engineer'}
person("Rolly", 23, city=extra['city'], job=extra['job'])
# 或者
person("Rolly", 23, **extra)

# 定义可变参数与关键字参数：
"""
*args 定义可变参数
**kw 定义关键字参数

"""
#!/bin/python3

"""
tuple与list很相似，也是有序列表，叫做元组，但是tuple一旦初始化后，不可更改
"""

classmates = ("Michael", "Rolly", "Adam")

print(classmates)

# truple 不可变，因此没有append/insert/pop等操作方法。但是访问是一致的
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 定义一个空的truple
t = ()


t = (1, 2)
print(t)

# 定义一个只有一个元素的truple
# 需要注意的是，如果想要定义只有一个元素的truple，使用(1) 是不可以的， 小括号() 即可以代表truple，也可以代码数学公式的小括号
# 所以就会产生歧义， 而Python规定，这种情况下是按照小括号进行计算。因此，表达一个元素的元组，需要多加一个逗号（,）
t = (1,)
print(t)

# 看一个可变的truple的例子
t = ('a', 'b', ['A', 'B'])
print(t)

t[2][0] = 'AA'
print(t)  

# 可以看出，最后结果为(a, b, [AA, B])，元素最终发生了改变。
# 之前提过， truple的元素是不可变的。
# 表面上看来，元组元素确实发生了变化。但其实，变化的并不是元组，而是list元素。而truple一开始指定的list列表，也并没有更改
# 所以，truple不变是指每个元素的指向或者地址不变。指向一个list，就不能改变指向其他对象，但指向的这个list是可变的。
#!/bin/python3

'''
__slots__: 定义特殊的__slots__变量，来限制该class 实例化后能添加的属性
'''

class Demo(object):
    __slots__ = ('name', 'age')


d = Demo()
d.name = 'Rolly'
d.age = 20

# 会报 AttributeError
# d.sex = 'male'

# 需要注意的是： __slots__只对当前类实例有效，对于继承的子类则不受影响
class Parc(Demo):
    pass

p = Parc()
p.name = 'Rolly'
p.age = 20
p.sex = 'female'

print(p.name)
print(p.age)
print(p.sex)

#!/bin/python3

'''
在OOP程序设计中，被继承的class称为基类、父类或超类
'''

class Animal(object):
    
    def run(self):
        print('Animal is running...')


class Cat(Animal):
    
    def run(self):
        print('Cat is running...')

class Dog(Animal):
    
    def run(self):
        print('Dog is running...')

c = Cat()
c.run()

d = Dog()
d.run()

# 判断变量类型可以是使用 isinstance()
# 由于Dog和Cat继承了Animal，所以我们也可以认为c同时也是Animal类型也没错。
print(isinstance(c, Animal))
print(isinstance(c, Cat))
print(isinstance(d, Animal))
print(isinstance(d, Dog))

a = Animal()

# 反过来后，尽快Dog和Cat继承了Animal，Animal的实例变量也不可能与Dog或Cat变量类型一致
print(isinstance(a, Dog))
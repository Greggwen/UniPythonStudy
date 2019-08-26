#!/bin/python3

"""
面向对象：Object Oriented Programming, OOP。
面向对象最重要的概念就是类（Class）和实例（Instance）。
"""

class Student(object):
    pass


print(Student)

s = Student()

s.name = "Rolly"

print(s.name)

'''
一般情况下，有些类需要强制绑定一些初始化的条件才可以实例化，为此类定义可能会包含名为__init__()的特殊方法。
定义了__init__()方法后，在实例化时会自动为新创建的类实例化调用
需要注意的： __init__()方法的第一个参数永远都是self，代表创建的实例本身
'''

class Teacher(object):

    def __init__(self, name):
        self.name = name

t = Teacher('Rolly')

print(t.name)
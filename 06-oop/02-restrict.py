#!/bin/python3

class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 若想获取私有变量的内容
    def get_name(self):
        print(self.__name)

    def get_score(self):
        print(self.__score)

    # 若想设置私有变量的内容
    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score



s = Student("Rolly", 100)

s.print_score()

# 以__为前缀的变量表示内部属性不能被外部访问
# print(s.__name)

s.get_name()
s.get_score()

s.set_name("Rolly And Kit")
s.get_name()
s.set_score(98)
s.get_score()
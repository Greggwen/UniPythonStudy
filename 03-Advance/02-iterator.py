#!/bin/python3

"""
迭代器：是Python最强大的功能之一，是访问元素集合的方式之一。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完成，迭代器只能往前不能后退。
迭代器的两个基本方法：iter() 和 next()
"""

list = [1, 2, 3, 4]
it = iter(list)

print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 若访问到最后一个元素后，依旧执行next() 则会提示报错
# print(next(it))

list1 = [2, 3, 4, 5]
it1 = iter(list1)
for x in it1:
    print(x, end=" ")


# 凡是可作用于for循环的对象都是iterable类型
# 凡是可作用于next()函数对象的都是Iterator类型
# 集合数据类型如list,dict,str等是iterable类型但不是iterator，不过可以通过iter()函数获得一个Iterator对象
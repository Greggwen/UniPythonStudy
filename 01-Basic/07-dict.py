#!/bin/python3

"""
dict 是Python内置字典，使用key-value形式，具有极快的查找速度
dict 是无序的，与key放入的顺序也无任何关系
dict 查找和插入速度极快，不会随着key的增加而变慢。
dict 会占用大量的内存，内存浪费会比较多。
相对list: list查找和插入的时间随着元素的增加而增加；占用空间少，内存浪费少。
"""
d = {'Michael': 95, 'Rolly': 100, 'Bob': 94}

print('Michael scores is %d' % (d['Michael'], ))
print('Rolly scores is %d' % (d['Rolly'], ))
print('Bob scores is %d' % (d['Bob'], ))

# 判断key是否存在，需要使用in关键字
if 'Joe' in d:
    print('Hello Joe')
else:
    print("Joe is not exists")

# 通过get()方法获取
print(d.get("Rolly"))

# 获取不存在的key，返回None
print(d.get("Joe"))

# 使用pop(key)删除指定元素, 当key不存在时，则会报错。
d.pop("Bob")
print(d)
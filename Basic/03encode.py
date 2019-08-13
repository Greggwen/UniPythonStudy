#!/bin/python3

"""
1、 一个字节能表示的最大整数是255（二进制11111111 = 十进制255）
2、 两个字节可以表示的最大整数是65535， 四个字节表示的最大整数是 4294967295
"""

print("包含中文的str")
# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord("中"))
print(chr(20013))

# 十六进制
print('\u4e2d\u6587')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
x = b'ABC'
print(x)

# print('你好'.encode('ascii'))  # 报错
print('你好'.encode('utf-8'))

# 字符串的长度
print(len("ABC"))
print(len("中文"))
print(len("中文".encode('utf-8')))

# 格式化输出, 在Python中，采用的格式化方式和C语言是一致的，用%实现
# 如果不确定使用什么占位符，可以使用%s。
# 若需要输出%，则需要使用%%表示
"""
占位符	替换内容
%d	    整数
%f	    浮点数
%s	    字符串
%x	    十六进制整数
"""

print("hello %s" % 'Python')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))


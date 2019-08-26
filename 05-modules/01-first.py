#!/bin/python3

'''
Python 本身内置很多非常有用的模块，可以拿来即用，例如： os， sys等模块，直接使用import os导入即可使用，无须再安装。
导入模块后，我们就有了变量指向该模块，利用这个变量，我们就可以访问该模块中的所有功能
'''

__author__ = 'Greewenly'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello World")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print('Too many arguments!')


if __name__ == "__main__":
    test()


'''
安装第三方模块：使用pip命令，例如： pip install moduleName。 pip需要注意使用的python版本。
'''
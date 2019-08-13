#!/bin/python3
import platform

"""
在这里需要注意的是： python3.x 源码文件默认使用utf-8编码，所以可以正常解析中文。
而python 2.x默认编码格式是 ASCII 格式，所以如果使用中文需要在开头添加： # -*- coding: UTF-8 -*-  或者  # coding=utf-8
# coding=utf-8
"""

print("Hello Python!")
print("你好，Python3")

# 查看Python 版本信息
print("使用Python当前版本为： " + platform.python_version())

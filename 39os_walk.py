#!/usr/bin/env python3
# coding: utf-8

"""os.walk()用法."""

import os


# dirpath是字符串, 当前路径名
# dirnames是列表, 当前路径名下的目录
# filenames是列表, 当前路径名下的文件
# dirnames和filenames不能同时都有内容
for dirpath, dirnames, filenames in os.walk('.'):
    #print(dirpath, dirnames, filenames)
    pass



# 打印socket目录和multiprocess目录下的文件夹和文件
for dirpath, dirnames, filenames in os.walk('.'):
    if dirpath == './socket':
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
        for filename in filenames:
            print(os.path.join(dirpath, filename))
    elif dirpath == './multiprocess':
        for dirname in dirnames:
            print(os.path.abspath(os.path.join(dirpath, dirname)))
        for filename in filenames:
            print(os.path.abspath(os.path.join(dirpath, filename)))

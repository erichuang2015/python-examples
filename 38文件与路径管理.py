#!/usr/bin/env python3
# coding: utf-8

import os


# 获取当前路径
os.getcwd()
# 列出当前路径下所有文件
os.listdir('.')
# 改变路径
os.chdir('..')

"""1.拆分路径"""
path = __file__ # 拿到的是绝对路径
# 返回一个文件路径和文件名组成的二元组
os.path.split(path)
# 返回文件的路径
os.path.dirname(path)
# 返回文件的文件名
os.path.basename(path)
# 返回一个除去文件拓展名的部分和拓展名组成的二元组
os.path.splitext(path)

"""2.构建路径"""
# 展开用户目录
os.path.expanduser('~')
# 得到文件的绝对路径
os.path.abspath('.')
# 拼接路径, 可以跨平台
os.path.join('~', 't', 'a.py')
#!/usr/bin/env python3
# coding: utf-8

import os


def main():
    # 获取当前路径
    print(os.getcwd())
    # 列出当前路径下所有文件
    print(os.listdir('.'))
    # 改变路径
    os.chdir('..')
    print(os.getcwd())
    print('*' * 50)

    """1.拆分路径"""
    # 拿到的是绝对路径
    path = __file__
    print(path)
    # 返回一个文件路径和文件名组成的二元组
    print(os.path.split(path))
    # 返回文件的路径
    print(os.path.dirname(path))
    # 返回文件的文件名
    print(os.path.basename(path))
    # 返回一个除去文件拓展名的部分和拓展名组成的二元组
    print(os.path.splitext(path))
    print('*' * 50)

    """2.构建路径"""
    # 展开用户目录
    print(os.path.expanduser('~'))
    # 得到文件的绝对路径
    print(os.path.abspath('.'))
    # 拼接路径, 可以跨平台
    print(os.path.join('~', 't', 'a.py'))
    print('*' * 50)


if __name__ == '__main__':
    main()

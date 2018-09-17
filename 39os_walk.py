#!/usr/bin/env python3
# coding: utf-8

"""`os.walk()` 用法。"""

import os


def print_all(path='.'):
    # dirpath是字符串, 当前路径名
    # dirnames是列表, 当前路径名下的目录
    # filenames是列表, 当前路径名下的文件
    # dirnames和filenames不能同时都有内容
    for dirpath, dirnames, filenames in os.walk(path):
        print(dirpath, dirnames, filenames)


def print_specified_dir(path='.'):
    """打印socket目录和multiprocess目录下的文件夹和文件."""

    for dirpath, dirnames, filenames in os.walk(path):
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


def print_all_dir(path='.'):
    """打印当前目录下所有文件夹."""

    for dirpath, dirnames, filenames in os.walk(path):
        if dirnames:
            for dirname in dirnames:
                print(dirname)


def print_all_file(path='.'):
    """打印当前目录下所有文件."""

    for dirpath, dirnames, filenames in os.walk(path):
        if filenames:
            for filename in filenames:
                print(filename)


if __name__ == '__main__':
    print_all()

#!/usr/bin/env python3
# coding: utf-8

"""上下文装饰器用法."""

from contextlib import contextmanager


@contextmanager
def open_flie(filename, mode, encoding='utf-8'):
    fp = open(filename, mode, encoding)
    try:
        yield fp
    finally:
        fp.close()
# try之前的是`__enter__`执行的
# try中的是as的内容, 可以yield一个空值
# finally是`__exit__`执行的


# 例子
@contextmanager
def cd(path):
    old_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield # 可以就写一个yield
    finally:
        os.chdir(old_cwd)

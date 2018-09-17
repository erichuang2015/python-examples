#!/usr/bin/env python3
# coding: utf-8

"""
__repr__属性决定了交互式环境中显示的内容.
__str__属性则是决定print时打印内容.
"""


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # !r 的意义
        # 如果name是个字符串, 那么会自动为它加上单引号
        # 否则, 比如说是数字, 则不加单引号
        # 这样就可以区分 int 和 str
        return '{}({!r})'.format(self.__class__.__name__, self.name)
        # 或
        #return '%s(%r)' % (self.__class__.__name__, self.name)

    def __str__(self):
        return '{}'.format(self.name)

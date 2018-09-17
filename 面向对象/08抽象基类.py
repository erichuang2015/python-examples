#!/usr/bin/env python3
# coding: utf-8

"""
内置的collections.abc模块定义了一系列抽象基类,
它们提供了每一种容器类型所应具备的常用方法,
从这样的基类中继承了子类之后, 如果忘记某个方法,
那么collections.abc模块就会指出这个错误.
如果子类已经实现了抽象基类所要求的每个方法,
那么基类就会提供剩下的那些方法.
"""

from collections.abc import Sequence


# collections.abc模块会指出缺少的魔法方法
class BadType(Sequence):
    pass
#foo = BadType()


# 如果子类已经实现了抽象基类所要求的每个方法，基类就会提供剩下的那些方法
class SequenceNode(Sequence):
    def __len__(self):
        pass

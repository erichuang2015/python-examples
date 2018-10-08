#!/usr/bin/env python3
# coding: utf-8

"""继承中的静态方法和类方法."""


class A:
    @staticmethod
    def hello():
        print('A: hello, world!')

    @classmethod
    def haha(cls):
        print('A: haha!')


class B(A):
    pass


class C(A):
    # 继承修改静态方法, 不需要再加`@staticmethod`装饰器
    # 但建议还是加上
    @staticmethod
    def hello():
        print('C: hello, world!')

    # 继承修改类方法, 需要加`@classmethod`装饰器
    @classmethod
    def haha(cls):
        print('C: haha!')


class D(object):
    """普通类."""
    def __init__(self):
        pass

    def hello():
        """奇怪, 这里没加self, 却能正常调用, 可能解释器把它当成了静态方法.

        原因：没用到self，默认当成静态方法
        """
        print('D: hello, world!')

    def haha(self):
        print('D: haha!')


def test():
    A.hello()
    A.haha()
    B.hello()
    B.haha()
    C.hello()
    C.haha()
    D.hello()
    # D.haha()  # D.haha(123) 可以


if __name__ == '__main__':
    test()

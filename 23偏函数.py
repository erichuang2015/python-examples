#!/usr/bin/env python3
# coding: utf-8

"""偏函数。
减少传入的参数数量，或用于 key，且不能传参数的情况。
"""

from functools import partial


def add(a=1, b=2):
    return a + b


def main():
    add2 = partial(add, b=10)
    c = add2(3)
    print(c)


if __name__ == '__main__':
    main()

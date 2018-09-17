#!/usr/bin/env python3
# coding: utf-8

"""具名元组。
"""

from collections import namedtuple


def main():
    # 字符串'Point'决定了，打印出来的名字
    # Point = namedtuple('Point', ('x', 'y'))
    # 或传入字符串, 参数之间用空格分开
    Point = namedtuple('Point', 'x y')
    p = Point(1, 2)
    print(p)
    print(p.x, p.y)
    # 返回Point拥有的字段, 是一个元组
    print(Point._fields)
    # 以collections.OrderedDict的形式返回
    print(p._asdict())


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# coding:utf-8

from collections import namedtuple


# 字符串'Point'决定了，打印出来的名字
Point = namedtuple('Point', ('x', 'y'))
p = Point(1, 2)
print(p)
print(p.x, p.y)
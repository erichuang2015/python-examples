#!/usr/bin/env python3
# coding: utf-8

"""从一个集合中获得最大或者最小的 N 个元素列表.

如果 N=1, 那么用min()或max()会更快些.
如果 N 的个数接近列表的长度, 那么用排序再切片会更快些.
其他情况, 堆排后再取值, 会更快.
"""

import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]


# 两个函数都能接受一个关键字参数, 用于更复杂的数据结构中
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

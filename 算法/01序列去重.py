#!/usr/bin/env python3
# coding: utf-8

"""序列去重方法。
"""


def dedupe(items):
    """序列去重，并保持有序，元素必须可哈希。"""

    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    """序列去重，并保持有序，元素不用可哈希。
    
    key 接收一个函数，计算出用来去重的值。
    """

    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item


def main():
    lst = [1, 1, 2, 3, 4, 5, 3, 4, 5, 2]
    print('去重前：')
    print(lst)
    print('去重后：')
    print(list(dedupe(lst)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# coding: utf-8

"""defaultdict 用法示例，注意和普通字典比较。
"""

from collections import defaultdict


def log_missing():
    print('key added')
    return 0


def increment_with_report(current, increments):
    """统计有多少个缺失的键。"""

    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


def main():
    current = {'green': 12, 'blue': 3}
    increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9),
    ]
    result = defaultdict(log_missing, current)
    print('Before:', dict(result))
    for key, amount in increments:
        # 当 result 中不存在该 key 时，会调用 log_missing 函数
        # 打印 'key added'，并把该 key 的值设为 0
        result[key] += amount
    print('After:', dict(result))


if __name__ == '__main__':
    main()

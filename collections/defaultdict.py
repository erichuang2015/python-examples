#!/usr/bin/env python3
# coding: utf-8

"""defaultdict用法示例，注意和普通字典比较."""

from collections import defaultdict


def log_missing():
    print('key added')
    return 0


# 统计有多少个缺失的键
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


if __name__ == '__main__':
    current = {'green': 12, 'blue': 3}
    increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9),
    ]
    result = defaultdict(log_missing, current)
    print('Before:', dict(result))
    for key, amount in increments:
        # 当result中不存在该key时，会调用log_missing函数
        # 打印'key added'，并把该key的值设为0
        result[key] += amount
    print('After:', dict(result))

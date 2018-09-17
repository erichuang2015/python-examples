#!/usr/bin/env python3
# coding: utf-8

"""随机模块。
"""

import random


def main():
    values = [1, 2, 3, 4, 5, 6]

    # 从序列中随机选一个元素
    print(random.choice(values))

    # 随机提取出序列中 N 个元素
    print(random.sample(values, 2))

    # 打乱序列顺序
    random.shuffle(values)
    print(values)

    # 生成 [x, y] 间的随机整数
    print(random.randint(0, 2))

    # 生成 0 到 1 范围内均匀分布的浮点数
    print(random.random())


if __name__ == '__main__':
    main()

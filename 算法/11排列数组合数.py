#!/usr/bin/env python3
# coding: utf-8

"""计算组合数或排列数。

permutations 排列数区分顺序。
combinations 组合数不区分顺序。
"""

from itertools import permutations, combinations


def main():
    s = 'A, B, C'
    s1 = s.replace(',', ' ').split()

    # permutations 排列数
    for item in permutations(s1):
        print(','.join(item))
    print('*' * 50)

    # combinations 组合数
    for item in combinations(s1, r=2):
        print(','.join(item))
    print('*' * 50)


if __name__ == '__main__':
    main()

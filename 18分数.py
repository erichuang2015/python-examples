#!/usr/bin/env python3
# coding: utf-8

"""Python 中的分数。
"""

from fractions import Fraction


def main():
    a = Fraction(5, 4)
    b = Fraction(7, 16)

    print(a + b)
    print(a * b)
    print('*' * 50)

    c = a * b
    print(c.numerator)  # 分子
    print(c.denominator)  # 分母
    print('*' * 50)

    # 转换成小数
    print(float(c))
    print('*' * 50)


if __name__ == '__main__':
    main()

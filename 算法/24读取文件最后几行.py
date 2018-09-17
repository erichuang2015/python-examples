#!/usr/bin/env python3
# coding: utf-8

"""用 deque 实现读取文件最后 n 行。"""

from collections import deque
from collections import Iterator, Iterable


if __name__ == '__main__':
    with open('00test.py') as f:
        # deque第一个参数接收一个可迭代对象
        # 只保留最后5行
        last_n_lines = deque(f, maxlen=5)
    # 可以被 for 作用的称为可迭代对象, Iterable
    print(isinstance(last_n_lines, Iterable))
    # 可以被 next() 函数调用并不断返回下一个值的对象称为迭代器, Iterator
    print(isinstance(last_n_lines, Iterator))
    for line in last_n_lines:
        # line中已有换行符, 所以把print自带的换行符去掉
        print(line, end='')

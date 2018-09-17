#!/usr/bin/env python3
# coding: utf-8

"""`deque` 用法。

对 `deque` 进行两端操作会非常快。

`deque` 可以指定保存的最大元素个数，
利用这个特性可以保留文件的最后几行。
"""

from collections import deque


def main():
    # 指定 deque 的大小
    # 如果不指定 maxlen 参数，那么会创建一个无限大小的 `deque`
    d = deque(maxlen=3)
    # 往最右边添加元素
    d.append(1)
    d.append(2)
    d.append(3)
    # 往最左边添加元素
    d.appendleft(4)
    # 最多只会保存最后添加的 maxlen 个元素
    print(d)
    print('*' * 50)

    # 弹出最右边的元素
    d.pop()
    # 弹出最左边的元素
    d.popleft()
    print(d)
    print('*' * 50)


if __name__ == '__main__':
    main()

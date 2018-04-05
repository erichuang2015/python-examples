#!/usr/bin/env python3
# coding:utf-8

from collections import deque


"""保存最后n个元素"""
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
d.append(4)
# 最多只会保存最后3个元素
print(d)

"""待补充"""
#!/usr/bin/env python3
# coding:utf-8

r'''统计字符串单词出现次数，不区分大小写'''

import re


pattern = re.compile(r'[,.!?]')


r'''第一种方式, 自定义算法.'''
s = 'I love python, python is simple and powerful!'
d = dict()
for letter in pattern.sub(' ', s.lower()).split():
    d[letter] = d.get(letter, 0) + 1
print(sorted(d.items(), key=lambda x:x[1], reverse=True))
# 打印出现次数最多的单词
print(max(d.items(), key=lambda x:x[1])[0])


r'''第二种方式, 使用Counter.'''
from collections import Counter
print(Counter(pattern.sub(' ', s.lower()).split()))


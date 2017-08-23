#!/usr/bin/env python3
# coding:utf-8

import sys
import time


def load1():
    r'''打印进度条.'''

    for i in range(100):
        # sys.stdout.write('>')
        # sys.stdout.flush()
        # 等价上面两句
        print('>', end='', flush=True)
        time.sleep(0.03)


def load2():
    r'''打印百分比.'''
    
    for i in range(100):
        # sys.stdout.write('\r%s%%'%(i+1))
        # sys.stdout.flush()
        # 等价上面两句
        print('\r%s%%'%(i+1), end='', flush=True)
        time.sleep(0.03)


def load3():
    r'''打印进度条和百分比.'''

    for i in range(100):
        k = i + 1
        s = '>'*i + ' '*(100-k)
        sys.stdout.write('\r' + s + '[%s%%]'%(i+1))
        sys.stdout.flush()
        time.sleep(0.03)


def load4():
    r'''让进度条短一些.'''

    for i in range(100):
        k = i + 1
        s = '>' * (i // 2) + ' ' * ((100 - k) // 2)
        sys.stdout.write('\r' + s + '[%s%%]' % (i + 1))
        sys.stdout.flush()
        time.sleep(0.03)


if __name__ == '__main__':
    load4()
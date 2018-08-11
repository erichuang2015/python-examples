#!/usr/bin/env python3
# coding: utf-8

"""
经测试, 
多进程中：
这三个退出函数都不能用于多进程中的子进程退出，
目前发现只能依靠异常来退出子进程。

多线程中：
exit() 可以退出当前线程
os._exit() 可以退出整个进程

"""

import os
import sys


def main():
    try:
        print('main')
        # exit(0)  # 其实是退出当前线程
        # os._exit(0)  # 退出整个进程，并且不会执行finall
        sys.exit(1)  # 感觉和 exit() 一样
    finally:
        print('finally')


if __name__ == '__main__':
    main()

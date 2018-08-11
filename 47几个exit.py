#!/usr/bin/env python3
# coding: utf-8

"""经测试, 这三个退出函数都不能用于多进程中的子进程退出.
目前发现只能依靠异常来退出子进程.
"""

import os
import sys


def main():
    try:
        print('main')
        # exit(0)
        # os._exit(0)  # 不会执行finally, 直接退出
        sys.exit(1)
    finally:
        print('finally')


if __name__ == '__main__':
    main()

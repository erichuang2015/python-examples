#!/usr/bin/env python3
# coding: utf-8

"""
经测试, 
多进程中：
这三个退出函数都不能用于多进程中的子进程退出，
目前发现只能依靠异常来「退出」子进程，
而且也不是完全的退出，会阻塞在那里，等待父进程退出。

多线程中：
exit()      可以退出当前线程
sys.exit()  感觉和 exit() 一样
os._exit()  可以退出整个进程，并且不会进行清理工作
"""

import os
import sys


def main():
    try:
        print('main')
        exit(0)  # 其实是退出当前线程
        sys.exit(1)  # 感觉和 exit() 一样
        os._exit(0)  # 退出整个进程，并且不会执行finall
    finally:
        print('finally')


if __name__ == '__main__':
    main()

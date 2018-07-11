#!/usr/bin/env python3
# coding: utf-8

"""进程间通信, 用Queue类.

可以看到, 两个进程是同步的.
"""

import os
import time
import random
from multiprocessing import Process, Queue


def write(q):
    """写数据进程."""
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D', 'E']:
        print('Put %s to queue...' % value)
        q.put(value)
        # 这里的时间是随机的
        time.sleep(random.randint(1, 2))


def read(q):
    """读数据进程."""

    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue, 并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw, 写入
    pw.start()
    # 启动子进程pr, 读取
    pr.start()
    # 打印当前父进程ID，可以看到一共有三个进程，父进程负责调控
    print('Main process: %s' % os.getpid())
    # 等待pw结束
    pw.join()
    # pr进程里是死循环, 无法等待其结束, 只能用terminate()方法强行终止
    pr.terminate()
    print("[End]")

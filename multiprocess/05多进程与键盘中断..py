#!/usr/bin/env python3
# coding: utf-8"""

"""多进程与键盘中断.

一次键盘中断, 会向所有父子进程发送KeyboardInterrupt异常,
所以父子进程都需捕获.

TODO
一个问题.
当一个子进程先退出(无论正常或异常)时, 再按键盘中断, 会抛出异常, 原因未知.
"""

import os
import sys
import time
import random
from multiprocessing import Pool


def long_time_task(name):
    try:
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(random.randint(4, 10))
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    except KeyboardInterrupt: # 这里不要指定异常名, 会捕获所有异常
        t, v, tb = sys.exc_info()
        print(t)
    finally:
        print('Child process %s' % name)


if __name__ == '__main__':
    CHILD_PROCESS_NUMBER = 8
    print('Parent process id is %s.' % os.getpid())
    p = Pool(CHILD_PROCESS_NUMBER)
    for i in range(CHILD_PROCESS_NUMBER):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close() # 调用 close() 之后就不能继续添加新的 Process 了
    try:
        p.join() # join()等待所有子进程结束
    except KeyboardInterrupt: # 一次键盘中断, 所有父子进程都会收到
        p.join() # 这里必须再加个join(), 不然父进程有可能先结束
    print('Parent process done.')

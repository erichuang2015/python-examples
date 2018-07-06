#!/usr/bin/env python3
# coding: utf-8"""

"""多进程与键盘中断.

一次键盘中断, 会向所有父子进程发送KeyboardInterrupt异常,
所以父子进程都需捕获
"""

import os
import sys
import time
import random
from multiprocessing import Pool


def exit_test():
    raise SystemError # 子进程中用exit()会阻塞?


def long_time_task(name):
    try:
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(random.randint(5, 10))
        end = time.time()
        exit_test()
    except KeyboardInterrupt:
        pass
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
        pass
    print('Parent process done.')
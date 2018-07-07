#!/usr/bin/env python3
# coding: utf-8"""

"""多进程同步, 使用multiprocessing模块的Lock类.

注意观察每个线程的运行时间, 应该依次加2s.
"""

import os
import time
import traceback
from multiprocessing import Pool, Lock


lock = Lock()


def print_hello():
    global lock
    lock.acquire() # 获取锁
    time.sleep(2)
    print('hello, world!')
    lock.release() # 释放锁


def long_time_task(name):
    try:
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        print_hello()
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    except: # 这里不要指定异常名, 会捕获所有异常
        traceback.print_exc()
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
    except KeyboardInterrupt:
        pass
    print('Parent process done.')

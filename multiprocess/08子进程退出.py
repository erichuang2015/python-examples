#!/usr/bin/env python3
# coding: utf-8"""

"""TODO 尝试多进程中的子进程单独退出.

多进程中, 当一个子进程结束时, 它不会立即退出(ps中查看还存在),
需等待所有其他子进程结束后, 才会真正退出.

当一个子进程先退出(无论正常或异常)时, 再按键盘中断, 会抛出异常.

看看能不能实现结束后真正退出, 从而解决这个问题.
"""

import os
import sys
import time
import random
import signal
from multiprocessing import Pool


def kill_self(signal):
    print(123)
    os.kill(os.getpid(), signal)
    print(456)


def long_time_task(name):
    try:
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(random.randint(3, 10))
        kill_self(signal.SIGINT)
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    except:  # 这里不要指定异常名, 会捕获所有异常
        t, v, tb = sys.exc_info()
        print(t)
    finally:
        print('Child process %s' % name)


if __name__ == '__main__':
    CHILD_PROCESS_NUMBER = 2
    print('Parent process id is %s.' % os.getpid())
    p = Pool(CHILD_PROCESS_NUMBER)
    for i in range(CHILD_PROCESS_NUMBER):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  # 调用 close() 之后就不能继续添加新的 Process 了
    try:
        p.join()  # join()等待所有子进程结束
    except KeyboardInterrupt: # 一次键盘中断, 所有父子进程都会收到
        p.join()  # 这里必须再加个join(), 不然父进程有可能先结束
    print('Parent process done.')

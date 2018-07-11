#!/usr/bin/env python3
# coding: utf-8"""

"""打印异常.

由于多进程中, 子进程出现异常不会打印异常信息, 会直接退出,
可以用这种方法获取异常信息.
"""

import os
import sys
import traceback
import time
from multiprocessing import Pool


def long_time_task(name):
    try:
        print('Run task %s (%s)...' % (name, os.getpid()))
        start = time.time()
        time.sleep(6)
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    except:  # 这里不要指定异常名, 会捕获所有异常
        # 1.打印异常类名
        t, v, tb = sys.exc_info()
        print(t)
        # 2.打印异常完整异常信息
        # traceback.print_exc()
        # 等价下面
        # traceback.print_exception(*sys.exc_info())
        # 3.不打印, 拿到上面的字符串
        s = traceback.format_exc()
        print(s)
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

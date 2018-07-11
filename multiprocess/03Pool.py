#!/usr/bin/env python3
# coding: utf-8

"""Pool类的apply_async()方法.

如果要启动大量的子进程, 可以用进程池的方式批量创建子进程,
multiprocessing模块Pool类提供了该功能.
"""

import os
import time
from multiprocessing import Pool


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(2)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 可以同时跑4个进程
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    # 对 Pool 对象调用 join() 方法会等待所有子进程执行完毕
    # 调用 join() 之前必须先调用 close()，否则报错
    # 调用 close() 之后就不能继续添加新的 Process 了
    # 这里不调用join，会马上结束，和map方法不同
    p.join()
    # 多次调用close和join，发现并不会报错
    # p.close()
    # p.join()
    print('All subprocesses done.')

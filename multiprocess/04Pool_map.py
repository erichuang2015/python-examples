#!/usr/bin/env python3
# coding:utf-8

"""Pool类map方法.

map方法会先把传入的生成器转换成列表，所以说不能传入无限大小的生成器！
apply_async方法虽然不会马上把生成器转换成列表，
但是主线程会一直for循环读生成器中的内容，不会说进程池满了以后就等待，
所以也有可能卡死！而且似乎出现异常退出后，屏幕不会打印任何信息，
会直接继续开启下一个进程，这点很不好

总结：不要传入无限大小的生成器，优先使用map方法
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
    # Pool 的默认大小是 CPU 的核数
    with Pool() as p:
        # map方法简化了进程池的调用
        # 并且不需要调用close方法和join方法
        p.map(long_time_task, range(8))
        p.terminate()
        p.join()
    print('All subprocesses done.')


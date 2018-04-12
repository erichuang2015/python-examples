#!/usr/bin/env python3
# coding:utf-8

"""threading模块的Thread类.

和multiprogress模块的Process类很相似
"""

import time
import threading


# 新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    for n in range(1, 6):
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join() # join()方法可以传入timeout参数
    print('thread %s ended.' % threading.current_thread().name)
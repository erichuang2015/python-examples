#!/usr/bin/env python3
# coding: utf-8

"""threading模块的Thread类

API和multiprogress模块的Process类相似。

每个线程的异常，单独处理。
但只有主线程能捕获 KeyboardInterrupt 异常

exit() 可以退出当前线程

注意python没有提供终止线程的API，
如需退出子线程，
将子线程 Daemon属性设为True，
这样主线程退出后，子线程也会退出。
或者设置一个 `_running` 属性
循环条件为 `while _running`，
在主线程中将`_running`设为False，
这样循环开始时，线程就会结束，
缺点就是线程不能立即结束，
但与上面一种方法比，可以进行线程结束后的清理工作
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
    t.setDaemon(True)
    t.start()
    try:
        t.join()  # `join()` 方法可以传入 `timeout` 参数
    except KeyboardInterrupt:
        print(123)
    finally:
        print(456)
    print('thread %s ended.' % threading.current_thread().name)

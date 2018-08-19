#!/usr/bin/env python3
# coding: utf-8

"""threading模块的Thread类。

每个线程的异常，单独处理。
但只有主线程能捕获 KeyboardInterrupt 异常。
每个子线程的异常要在 `run()` 中捕获，
而不能在主线程中捕获。

可以用 `atexit.register(self.close)` 给子线程注册清理函数，
让子线程退出时进行清理工作。

`exit()` 可以退出当前线程。

如果某个子线程的 daemon 属性为 False，主线程结束时会检测该子线程是否结束，
如果该子线程还在运行，则主线程会等待它完成后再退出；
如果某个子线程的 daemon 属性为 True，
主线程结束时不对这个子线程进行检查而直接退出，
同时所有 daemon 值为 True 的子线程将随主线程一起结束，而不论是否完成。
daemon 属性的值默认为 False 。

注意 python 没有提供主线程终止子线程的 API，
如需退出子线程，
先将子线程 Daemon 属性设为 True，
这样主线程退出后，子线程也会退出，
可以主线程退出前进行一些保存工作。
"""

import threading
import time
import random
import os
import sys
import atexit

THREAD_NUM = 2


class MyThread(threading.Thread):
    def __init__(self, threadname, daemon):
        super().__init__(name=threadname, daemon=daemon)

        atexit.register(self.close)  # 注册清理函数，线程结束时自动调用

        self._running = True

        self.num = 0

    def run(self):
        print('%s: start!' % self.name)

        # 每个子线程的异常要在 `run()` 中捕获，
        # 而不能在主线程中捕获。
        try:
            while self._running:
                print('%s: %s' % (self.name, self.num))
                self.num += random.randint(1, 6)
                time.sleep(self.num)
                raise EOFError  # 模拟抛出异常
        except:
            t, v, tb = sys.exc_info()
            print(t)

    def terminate(self):
        self._running = False

    def save(self):
        """进行一些保存工作"""

        print('save num %s' % self.num)

    def close(self):
        """进行一些清理工作"""

        print('close %s' % self.num)


def main():
    thread_list = []
    for i in range(THREAD_NUM):
        t = MyThread(f'thread{i+1}', daemon=True)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    start = time.time()
    try:
        for t in thread_list:
            t.join()
    except KeyboardInterrupt:  # 只有主线程能收到键盘中断
        for t in thread_list:  # 防止下面在保存完后，线程又开始执行新一轮
            t.terminate()
        for t in thread_list:  # 保存未完成的子线程工作
            if t.is_alive():
                t.save()
    end = time.time()
    print('\n[Finished in %.2fs]\n' % (end - start))


if __name__ == '__main__':
    main()

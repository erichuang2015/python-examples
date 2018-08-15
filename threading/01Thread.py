#!/usr/bin/env python3
# coding: utf-8

"""threading模块的Thread类。

每个线程的异常，单独处理。
但只有主线程能捕获 KeyboardInterrupt 异常。
每个子线程的异常要在 `run()` 中捕获，
而不能在主线程中捕获。

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

THREAD_NUM = 2


class MyThread(threading.Thread):
    def __init__(self, threadname, daemon=False):
        super().__init__(name=threadname, daemon=daemon)
        self.num = 0

    def run(self):
        print('Thread %s: hello, world!' % self.name)
        # 每个子线程的异常要在 `run()` 中捕获，
        # 而不能在主线程中捕获。
        try:
            while True:
                print('Thread %s: %s' % (self.name, self.num))
                self.num += 1
                time.sleep(random.randint(1, 6))
                raise EOFError
        except:
            t, v, tb = sys.exc_info()
            print(t)

    def save(self):
        """进行一些保存工作"""

        print('save num %s' % self.num)


def main():
    thread_list = []
    # 线程名不能为 0，原因未知
    for i in range(1, THREAD_NUM+1):
        t = MyThread(i, daemon=True)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    try:
        for t in thread_list:
            t.join()
    except KeyboardInterrupt:
        print('等待子进程结束中...')
        for t in thread_list:  # 此时子线程还未结束，所以必须把未完成的工作保存下来
            if t.is_alive():
                t.save()

    print('over!')


if __name__ == '__main__':
    main()

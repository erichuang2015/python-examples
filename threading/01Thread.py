#!/usr/bin/env python3
# coding: utf-8

"""threading模块的Thread类。

每个线程的异常，单独处理。
但只有主线程能捕获 KeyboardInterrupt 异常。

exit() 可以退出当前线程。

如果某个子线程的 daemon 属性为 False，主线程结束时会检测该子线程是否结束，
如果该子线程还在运行，则主线程会等待它完成后再退出；
如果某个子线程的 daemon 属性为 True，
主线程结束时不对这个子线程进行检查而直接退出，
同时所有 daemon 值为 True 的子线程将随主线程一起结束，而不论是否完成。
daemon 属性的值默认为 False 。

注意python没有提供主线程终止子线程的API，
如需退出子线程，
先将子线程 Daemon属性设为True，
这样主线程退出后，子线程也会退出，
但也可以进行一些保存工作。

或者设置一个 `_running` 属性，
循环条件为 `while _running`，
在主线程中将`_running`设为False，
这样循环开始时，线程才会结束，比较温和。

两种退出方式都有自己的适用场景。
"""

import threading
import time
import random
import os

THREAD_NUM = 2


class MyThread(threading.Thread):
    def __init__(self, threadname, daemon=False):
        super().__init__(name=threadname, daemon=daemon)
        self._running = True
        self.num = 0

    def run(self):
        print('Thread %s: hello, world!' % self.name)
        # 线程对象的属性互不干扰
        while self._running:
            print('Thread %s: %s' % (self.name, self.num))
            self.num += 1
            time.sleep(2)

    def terminate(self):
        self._running = False

    def save(self):
        """进行一些保存工作"""

        print('save num %s' % self.num)


def main():
    thread_list = []
    # 线程名不能为 0，原因未知
    for i in range(1, THREAD_NUM+1):
        t = MyThread(i)
        thread_list.append(t)

    for t in thread_list:
        t.start()
    try:
        for t in thread_list:
            t.join()
    except KeyboardInterrupt:  # 会等待子线程走完当前一轮，才退出，比较温和
        print('等待子进程结束中...')
        for t in thread_list:
            t.terminate()
        for t in thread_list: # 这种方式退出线程，不需要将 `daemon` 设为 True
            t.join()  # join() 不能少
        for t in thread_list:
            t.save()
        
    print('over!')


if __name__ == '__main__':
    main()


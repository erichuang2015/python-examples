#!/usr/bin/env python3
# coding: utf-8

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

    def clean(self):
        """进行一些清理工作"""

        print('clean')


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
    except:
        for t in thread_list:
            t.terminate()
        for t in thread_list:
            t.join()  # join() 不能少
        for t in thread_list:
            t.clean()
        
    print('over!')


if __name__ == '__main__':
    main()

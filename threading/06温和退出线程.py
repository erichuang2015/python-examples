"""温和退出线程。

设置一个 `self._running` 属性，
循环条件为 `while self._running`，
在主线程中将`_running` 设为 False，
这样循环开始时，线程就会结束退出，比较温和。

这种方法，不需要将 `daemon` 设为 True，
因为主线程退出前，子线程都已经结束了。
"""

import threading
import time
import random
import os
import sys

THREAD_NUM = 2


class MyThread(threading.Thread):
    def __init__(self, threadname, daemon=False):
        super().__init__(name=threadname, daemon=daemon)
        self._running = True
        self.num = 0

    def run(self):
        print('Thread %s: hello, world!' % self.name)
        while self._running:
            print('Thread %s: %s' % (self.name, self.num))
            self.num += 1
            time.sleep(random.randint(1,6))

    def terminate(self):
        self._running = False


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
    except:  # 会等待子线程走完当前一轮，才退出，比较温和
        print('等待子进程结束中...')
        for t in thread_list:  # 将 `_running` 设为 False
            t.terminate()
        for t in thread_list:  # 等待子线程走完当前一轮
            t.join()
    for t in thread_list:
        print(t.getName(), t.is_alive())

    print('over!')


if __name__ == '__main__':
    main()


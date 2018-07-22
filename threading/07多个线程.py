#!/usr/bin/env python3
# coding: utf-8

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, threadname):
        super().__init__(name=threadname)

    def run(self):
        while True:
            print('%s: hello, world!', self.name)
            time.sleep(2)


def main():
    thread_list = []
    for i in range(1, 5):
        t = MyThread(i)
        thread_list.append(t)
    for t in thread_list:
        t.setDaemon(True)
        t.start()

    for t in thread_list:
        print(123)
        t.join()


if __name__ == '__main__':
    main()

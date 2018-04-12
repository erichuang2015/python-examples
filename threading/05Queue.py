#!/usr/bin/env python3
# coding:utf-8

"""queue模块的Queue类

使用Queue类实现线程同步,
尤其适合需要在多个线程之间进行信息交换的场合，
实现了多线程编程所需要的所有锁语义
"""

import threading
import time
import queue
from random import random


# 自定义生产者线程类
class Producer(threading.Thread):   
    def __init__(self, threadname):
        super().__init__(name=threadname)

    def run(self):
        global myqueue
        # 在队列尾部追加元素
        myqueue.put(self.getName())
        print(self.getName(), 'put', self.getName(), 'to queue')
        #time.sleep(0.5)


# 自定义消费者线程类
class Consumer(threading.Thread):
    def __init__(self, threadname):
        super().__init__(name=threadname)

    def run(self):
        # 设置一个随机等待时间
        time.sleep(random())
        global myqueue
        # 在队列首部获取元素
        print(self.getName(), 'get', myqueue.get(), 'to queue')


if __name__ == '__main__':
    myqueue = queue.Queue()
    plist = []
    clist = []
    for i in range(10):
        p = Producer('Producer' + str(i))
        plist.append(p)
        c = Consumer('Consumer' + str(i))
        clist.append(c)

    # 依次启动生产者线程和消费者线程
    for p, c in zip(plist, clist):
        p.start()
        p.join()
        c.start()
        # 如果在Consumer的run()方法中设置了一个随机等待时间，
        # 那么必须要使用join()方法才能实现现场同步
        c.join() 
#!/usr/bin/env python3
# coding: utf-8

"""
多线程和多进程最大的不同在于，
多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，全局变量都由所有线程共享，
所以，任何一个全局变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个全局变量，把内容给改乱了，
所以需要加锁。

**注意**：
线程获取锁后，若没有释放锁，就退出，
会导致其他线程永远也获取不了锁！
"""

import time
import threading


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self): # 重写run()方法
        global x
        # 先要获取锁
        # 当多个线程同时执行 lock.acquire() 时，
        # 只有一个线程能成功地获取锁，然后继续执行代码，
        # 其他线程就继续等待直到获得锁为止。
        lock.acquire()
        x = x + 3
        print(x)
        # 改完了一定要释放锁
        # 否则那些苦苦等待锁的线程将永远等待下去
        lock.release()

lock = threading.Lock()

# 存放多个线程的列表
t1 = []
for i in range(10):
    t = MyThread()
    t1.append(t)

# 多个线程互斥的访问变量
x = 0
# 启动列表中的所有线程
for i in t1:
    i.start()

#!/usr/bin/env python3
# coding: utf-8

"""Thread类的daemon属性, 表示线程是否为守护线程.

如果某个子线程的daemon属性为False, 主线程结束时会检测该子线程是否结束, 
如果该子线程还在运行, 则主线程会等待它完成后再退出;
如果某个子线程的daemon属性为True, 主线程结束时不对这个子线程进行检查而直接退出，
同时所有daemon值为True的子线程将随主线程一起结束, 而不论是否完成.

daemon属性的值默认为False, 如果需要修改, 则必须在调用start()方法启动线程前进行设置.
"""

import threading
import time


class mythread(threading.Thread):
    def __init__(self, num, threadname):
        super().__init__(name=threadname)
        self.num = num

    def run(self): # 重写run()方法
        time.sleep(self.num)
        print(self.num)


t1 = mythread(1, 't1')
t2 = mythread(5, 't2')
# t1.daemon = True
t2.daemon = True
print(t1.daemon)
print(t2.daemon)
t1.start()
t2.start()
# t2.join() # 调用join()方法后，主线程会等待t2执行完毕，否则一直往下执行
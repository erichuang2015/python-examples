#!/usr/bin/env python3
# coding:utf-8

r'''threading模块的Event类.'''

import threading


# 自定义线程类
class mythread(threading.Thread):
    def __init__(self, threadname):
        super().__init__(name=threadname)

    def run(self):
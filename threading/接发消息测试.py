#!/usr/bin/env python3
# coding:utf-8

"""
测试控制台接发消息的可行性
"""

import time
import threading


def recv_msg():
    while True:
        print('[小花]：你好！')
        time.sleep(2)


def send_msg():
    while True:
        msg = input()
        print('[我]: {}'.format(msg))


if __name__ == '__main__':
    t1 = threading.Thread(target=recv_msg)
    t2 = threading.Thread(target=send_msg)
    t1.start()
    t2.start()

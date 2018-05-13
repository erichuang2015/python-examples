#!/usr/bin/env python3
# coding: utf-8

from socket import socket, SOCK_DGRAM
from threading import Thread


def recv_msg():
    while True:
        msg, addr = s.recvfrom(1024)
        msg = msg.decode()
        print('[{}:{}]: {}'.format(addr[0], addr[1], msg))


def send_msg(target):
    while True:
        msg = input()
        s.sendto(msg.encode(), (target, 9527))


def main():
    global s
    s = socket(type=SOCK_DGRAM)
    s.bind(('', 9527))
    target = input('请输入目标IP：')
    t1 = Thread(target=recv_msg)
    t2 = Thread(target=send_msg, args=(target,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

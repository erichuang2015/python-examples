#!/usr/bin/env python3
# coding: utf-8

from socket import socket
from threading import Thread


def recv_msg():
    while True:
        msg = s.recv(1024).decode()
        print(msg)


def send_msg():
    while True:
        msg = input()
        s.sendall(msg.encode())


def main():
    global s
    s = socket()
    s.connect(('192.168.47.1', 9527))
    t1 = Thread(target=recv_msg)
    t2 = Thread(target=send_msg)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

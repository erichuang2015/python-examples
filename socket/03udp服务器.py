#!/usr/bin/env python3
# coding: utf-8

import socket


if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ('127.0.0.1', 9527)
    sk.bind(address)

    print('等待消息...')
    while True:
        data, addr = sk.recvfrom(4096)
        if not data:
            break
        recv_data = data.decode('utf-8')
        print(addr, recv_data)
    sk.close()
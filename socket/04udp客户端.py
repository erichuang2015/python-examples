#!/usr/bin/env python3
# coding: utf-8

import socket


if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ('127.0.0.1', 9527)

    while True:
        try:
            send_data = input()
        except EOFError:
            break
        sk.sendto(send_data.encode('utf-8'), address)
    sk.close()
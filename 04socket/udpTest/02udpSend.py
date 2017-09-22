#!/usr/bin/env python3
# coding:utf-8

import socket


# udp发送方
if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target_ip = input('目标IP地址: ')

    while True:
        send_data = input('>>> ')
        sk.sendto(send_data.encode('utf-8'), (target_ip, 9527))
        if send_data == 'byebye':
            break
    sk.close()
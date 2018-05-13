#!/usr/bin/env python3
# coding: utf-8

import socket


# udp接收方
if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 如果要绑定本机，切记主机号要填空，也不能绑定127.0.0.1
    sk.bind(('', 9527))

    print('等待消息...')
    while True:
        data,addr = sk.recvfrom(1024)
        recv_data = data.decode('utf-8')
        print(addr, recv_data)
        if recv_data == 'byebye':
            break
    sk.close()
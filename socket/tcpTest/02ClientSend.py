#!/usr/bin/env python3
# coding:utf-8

import socket


# 单线程tcp客户端（发送方）
if __name__ == '__main__':
    """
    AF_INET：使用IPv4地址和端口号
    SOCK_STREAM：面向连接，即tcp
    SOCK_DGRAM：面向非连接，即udp
    """
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务，设置连接的主机和端口号（端口号只能用int类型）
    host = input('请输入对方IP地址: ')
    # tcp相比较udp需要先于与目标服务器建立连接
    sk.connect((host, 9527))
    
    while True:
        # 向服务器发送消息
        send_data = input('>>> ')
        sk.send(send_data.encode('utf-8'))
        if send_data == 'byebye':
            break
    sk.close()
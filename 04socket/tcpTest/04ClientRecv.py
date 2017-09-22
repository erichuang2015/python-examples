#!/usr/bin/env python3
# coding:utf-8

import socket
import sys


if __name__ == '__main__':
    # 创建 socket 对象
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    host = '192.168.47.1'
    # 设置端口号
    port = 9999
    # 连接服务，指定主机和端口
    sk.connect((host, port))
    # 接收小于 1024 字节的数据
    msg = sk.recv(1024)
    print (msg.decode('utf-8'))

    sk.close()
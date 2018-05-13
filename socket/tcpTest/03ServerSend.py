#!/usr/bin/env python3
# coding: utf-8

import socket
import sys


if __name__ == '__main__':
    # 创建 socket 对象
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取本地主机名
    port = 9999
    # 绑定端口
    serversocket.bind(('', port))
    # 设置最大连接数，超过后排队
    serversocket.listen(5)
    
    print('等待客户端接入...')
    while True:
        # 建立客户端连接
        clientsocket,addr = serversocket.accept()
        print(" 连接地址 : %s" % str(addr))
        msg = '欢迎访问菜鸟教程！'
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()

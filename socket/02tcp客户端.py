#!/usr/bin/env python3
# coding: utf-8

"""简单tcp客户端.

发送字符串给目标服务器，并接受服务器返回的内容。
"""

import socket

BUF_SIZE = 4096


def main():
    # AF_INET: 使用IPv4地址和端口号
    # SOCK_STREAM: 面向连接, 即tcp
    # SOCK_DGRAM: 面向非连接, 即udp
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务, 设置连接的主机和端口号（端口号只能用int类型）
    address = ('127.0.0.1', 9527)
    # tcp相比较udp需要先于与目标服务器建立连接
    print('连接%s:%d中...' % address, end='')
    client_sock.connect(address)
    print('成功!')

    while True:
        try:
            send_data = input()
        except (EOFError, KeyboardInterrupt):  # 监测 C+d 和 C+c
            break
        client_sock.sendall(send_data.encode('utf-8'))
        recv_data = client_sock.recv(BUF_SIZE)
        if not recv_data:
            print('对方服务器', address, '已关闭')
            break
        print(recv_data.decode('utf-8'))
    client_sock.close()


if __name__ == '__main__':
    main()

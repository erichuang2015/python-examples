#!/usr/bin/env python3
# coding: utf-8

"""简单多线程tcp服务器.

将收到的字符串转为大写, 发回给客户端.
"""

import socket
import threading


BUF_SIZE = 4096


def thread_handler(cfd, cli_addr):
    print('已被连接:', cli_addr)
    while True:
        # 接收客户端消息
        recv_data = cfd.recv(BUF_SIZE)
        # 对端关闭, 则会返回空值
        if not recv_data:
            break
        cfd.sendall(recv_data.upper())
    print('对端关闭:', cli_addr)
    cfd.close()


def main():
    # AF_INET: 使用IPv4地址和端口号
    # SOCK_STREAM: 面向连接, 即tcp
    # SOCK_DGRAM: 面向非连接, 即udp
    lfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口号只能用int类型
    address = ('127.0.0.1', 9527)
    lfd.bind(address)
    # 设置最大连接数，超过后排队
    lfd.listen(1)

    # 等待客户端连接
    print('tcp等待连接中...')
    while True:
        t = threading.Thread(target=thread_handler, args=lfd.accept())
        t.start()
    lfd.close()


if __name__ == '__main__':
    main()

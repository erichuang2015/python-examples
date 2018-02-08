#!/usr/bin/env python3
# coding:utf-8

import socket


# 单线程tcp服务器（接收方）
if __name__ == '__main__':
    """
    AF_INET：使用IPv4地址和端口号
    SOCK_STREAM：面向连接，即tcp
    SOCK_DGRAM：面向非连接，即udp
    """
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 如果要绑定本机，切记主机号要填空，不要绑定127.0.0.1，端口号只能用int类型
    sk.bind(('', 9527))
    # 设置最大连接数，超过后排队
    sk.listen(5)

    # 等待客户端连接
    print('tcp等待连接...')
    client,addr = sk.accept()

    print('已被连接', addr)
    while True:
        # 接收客户端消息
        recv_data = client.recv(1024).decode()
        print('%s: %s' % (addr, recv_data))
        if recv_data == 'byebye':
            # 关闭与该客户端的连接
            client.close()
            break
    sk.close()

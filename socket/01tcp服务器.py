#!/usr/bin/env python3
# coding: utf-8

"""简单多线程tcp服务器.

将收到的字符串转为大写, 发回给客户端.
"""

import socket
import threading
import time


BUF_SIZE = 4


def thread_handler(cfd, cli_addr):
    print('已被连接:', cli_addr)
    while True:
        print('读数据')
        # recv() 接收客户端消息，只要缓冲区还有数据就会循环读，
        # 直到阻塞等待下一次请求，这时阻塞模式与非阻塞模式的唯一区别，
        # 若在非阻塞模式下，读到无数据时，会 `raise BlockingIOError`。
        # TCP Data 的长度 = IP 总长度 - IP Header 长度 - TCP Header 长度。
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
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 端口号只能用int类型
    address = ('127.0.0.1', 9527)
    server_sock.bind(address)
    # 设置最大连接数，超过后排队
    server_sock.listen(2)

    print('tcp等待连接中...')
    start = time.perf_counter()
    try:
        while True:
            client_sock, addr = server_sock.accept()
            t = threading.Thread(target=thread_handler, args=(client_sock, addr))
            # 设置线程daemon属性为True, 主线程不会等待该子线程退出后再退出
            # 该属性要在线程运行前设置
            t.daemon = True
            t.start()
    except KeyboardInterrupt:
        pass
    finally:
        server_sock.close()
        end = time.perf_counter()
        finished = end - start
        print('\n[Finished in %.3fs]\n' % finished)


if __name__ == '__main__':
    main()

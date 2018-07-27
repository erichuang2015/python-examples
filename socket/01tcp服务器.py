#!/usr/bin/env python3
# coding: utf-8

"""简单多线程tcp服务器.

将收到的字符串转为大写, 发回给客户端.
"""

import socket
import threading
import time

BUF_SIZE = 4096


def thread_handler(cfd, cli_addr):
    print('已被连接:', cli_addr)
    while True:
        # 接收客户端消息
        # **注意**: tcp无法判断到底要接收多少数据,
        # 所以无法保证完整读完数据,
        # 数据的长度规则是双方约定好的,
        # 如定义数据头, 定义尾字符,
        # 例子有http.
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
    # 端口复用
    lfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 端口号只能用int类型
    address = ('127.0.0.1', 9527)
    lfd.bind(address)
    # 设置最大连接数，超过后排队
    lfd.listen(2)

    print('tcp等待连接中...')
    start = time.perf_counter()
    try:
        while True:
            t = threading.Thread(target=thread_handler, args=lfd.accept())
            # 设置线程daemon属性为True, 主线程不会等待该子线程退出后再退出
            # 该属性要在线程运行前设置
            t.daemon = True
            t.start()
    except KeyboardInterrupt:
        pass
    finally:
        lfd.close()
        end = time.perf_counter()
        finished = end - start
        print('\n[Finished in %.3fs]\n' % finished)


if __name__ == '__main__':
    main()

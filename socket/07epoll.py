#!/usr/bin/env python3
# coding: utf-8

"""
LT模式: epoll默认模式, 只要缓冲区还有数据就会触发事件.
ET模式: 事件只触发第一次, 无论缓冲区是否还有数据, 所以有可能导致数据被丢弃.

详见下面例子.
"""

import socket
import select


def main():
    # 创建epoll
    epoll = select.epoll()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口复用
    server_socket.bind(('localhost', 9527))
    server_socket.listen(4)
    server_socket.setblocking(False)  # 服务端设置非阻塞

    # 注册监听server_socket
    # 第一个参数是：要监听的socket的文件描述符
    # 第二参数：要监听的事件类型
    # ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序, 应用程序必须立即处理该事件。下次将不会在通知。
    epoll.register(server_socket.fileno(), select.EPOLLIN | select.EPOLLET)
    # 文件句柄到所对应对象的字典，格式为{句柄：对象}
    socket_dict = {}

    try:
        while True:
            print('等待事件中...')
            # 如果有新的客户端和可以收数据的socket和断开的socket就解除阻塞, 并且返回列表
            epoll_list = epoll.poll()
            # [(3, 1)] 3是文件描述符, 1是有数据进来了
            print(epoll_list)

            # 轮询注册的事件集合, 返回值为[(文件句柄, 对应的事件), (...), ...]
            for fd, event in epoll_list:
                # 当有客户端连接的时候
                if fd == server_socket.fileno():
                    # 有新的客户端链接了
                    client_socket, client_address = server_socket.accept()
                    # 客户端也设置不阻塞
                    client_socket.setblocking(False)
                    # 当有新的链接就会创建新的sockect，也要注册到epoll中
                    epoll.register(client_socket.fileno(), select.EPOLLIN | select.EPOLLET)
                    # 加入字典, 用于读时取出文件描述符对应的套接字对象
                    socket_dict[client_socket.fileno()] = client_socket
                    print('已被连接:', client_address)
                # 当有客户端的数据发送过来的时候，会触发 EPOLLIN 事件
                else:
                    client_socket = socket_dict[fd]
                    buf = b''
                    try:
                        while True:  # 在 ET 模式下，需要循环读，直到缓冲区无数据
                            print('非阻塞读')
                            # 将接收缓冲区设的很小,
                            # 用于测试LT和ET模式
                            recv_data = client_socket.recv(4)
                            if not recv_data:
                                print('对端关闭:', client_socket.getpeername())
                                client_socket.close()
                                epoll.unregister(fd)
                                socket_dict.pop(fd)
                            buf += recv_data
                    except BlockingIOError:  # socket 设为非阻塞，缓存区无数据时读，会抛出这个异常
                            print(buf.decode())
                            client_socket.send(buf.upper())
    except KeyboardInterrupt:
        pass
    finally:
        for client_socket in socket_dict.values():
            client_socket.close()
        server_socket.close()
        epoll.close()
        print('关闭成功!')


if __name__ == '__main__':
    main()

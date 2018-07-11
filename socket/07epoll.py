#!/usr/bin/env python3
# coding: utf-8

import socket
import select


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 9527))
    server_socket.listen(5)
    # 服务端设置非阻塞
    server_socket.setblocking(False)
    # 创建epoll
    epoll = select.epoll()
    # 注册监听server_socket
    # 第一个参数是：要监听的socket的文件描述符
    # 第二参数：要监听的事件类型
    # ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。下次将不会在通知。
    epoll.register(server_socket.fileno(), select.EPOLLIN | select.EPOLLET)
    # 文件句柄到所对应对象的字典，格式为{句柄：对象}
    socket_list = {}
    try:
        while True:
            print('等待事件中...')
            # 如果有新的客户端和可以收数据的socket和断开的socket就解除阻塞，并且返回列表
            epoll_list = epoll.poll()
            # [(3, 1)] 3是文件描述符，1是有数据进来了
            print(epoll_list)

            # 轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
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
                    socket_list[client_socket.fileno()] = client_socket
                    print('已被连接:', client_address)
                # 当有客户端的数据发送过来的时候，会触发 EPOLLIN 事件
                elif event == select.EPOLLIN:
                    client_socket = socket_list[fd]
                    recv_data = client_socket.recv(1024)
                    if recv_data:
                        print(recv_data.decode())
                        client_socket.send(recv_data.upper())
                    else:
                        print('对端关闭:', client_socket.getpeername())
                        # 从epoll中删除文件描述符
                        epoll.unregister(fd)
                        # 从字典socket_list中删除
                        socket_list.pop(fd)
                        client_socket.close()
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# coding: utf-8

"""epoll 使用实例。

事件类型：
　　select.EPOLLIN    可读事件
　　select.EPOLLOUT   可写事件
　　select.EPOLLERR   错误事件名，这个事件是不需要专门注册的，默认就有，详见 `man epoll_ctl` 。
　　select.EPOLLRDHUP 客户端断开事件
　　select.EPOLLHUP  「 which signals an unexpected close of the socket,
                      i.e. usually an internal error 」，
                     这个事件是不需要专门注册的，默认就有。

LT模式：epoll 默认模式，只要缓冲区还有数据就会触发事件。
ET模式：事件只触发第一次，无论缓冲区是否还有数据，
       所以一旦触发，需要循环把缓冲区数据读完，
       这要求将 socket 设为非阻塞。

注意点：
当客户端连接本服务器时，会触发 select.EPOLLIN 。
当客户端有数据发送过来时，会触发 select.EPOLLIN 。
当对应 socket 发送缓冲区未满时，会触发 select.EPOLLOUT 。
当客户端关闭时，会触发 select.EPOLLIN | select.EPOLLRDHUP 。
"""

import socket
import select


class Manager:

    def __init__(self, address, max_events):

        self.address = address
        self.max_events = max_events

        # 创建epoll
        self.epoll = select.epoll()

        # 创建服务套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 服务端设置非阻塞
        self.server_socket.setblocking(False)
        # 端口复用
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(self.address)
        self.server_socket.listen(self.max_events)
        self.server_fd = self.server_socket.fileno()

        # 注册监听server_socket
        # 第一个参数是：要监听的socket的文件描述符
        # 第二参数：要监听的事件类型，这里设置 ET 模式
        self.epoll.register(self.server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

        # 文件句柄到所对应对象的字典，格式为{句柄：对象}
        self.fd_to_socket = {}
        # 缓存发送内容
        self.fd_to_buffer = {}

    def run(self):
        while True:
            print('等待事件中...')
            # `maxevents` 决定返回的列表最大长度，
            # 这次若没返回完，则下次 `poll()` 时返回
            events = self.epoll.poll(maxevents=self.max_events)

            # 轮询注册的事件集合, 返回格式为[(文件句柄, 对应的事件), ...]
            for fd, event in events:
                print('fd: {}, event: {}'.format(fd, event))

                # 当有客户端连接的时候，会触发 EPOLLIN 事件
                if fd == self.server_fd:
                    self.accept_handler()

                # 当有客户端的数据发送过来的时候，会触发 EPOLLIN 事件
                elif event == select.EPOLLIN:
                    self.read_handler(fd)

                # 当网络发送缓冲区未满，可以发送时，会触发 EPOLLOUT 事件
                elif event == select.EPOLLOUT:
                    self.write_handler(fd)

    def accept_handler(self):
        # 有新的客户端链接了
        client_socket, client_address = self.server_socket.accept()
        # 客户端也设置不阻塞
        client_socket.setblocking(False)
        # 当有新的链接就会创建新的sockect，也要注册到epoll中
        self.epoll.register(client_socket.fileno(), select.EPOLLIN | select.EPOLLET)
        # 加入字典，用于读时取出文件描述符对应的套接字对象
        self.fd_to_socket[client_socket.fileno()] = client_socket
        # 加入字典，用于读时取出文件描述符对应的缓冲区
        self.fd_to_buffer[client_socket.fileno()] = None

        print('已被连接:', client_address)

    def read_handler(self, fd):
        client_socket = self.fd_to_socket[fd]
        buffer = b''
        try:
            while True:  # 在 ET 模式下，需要循环读，直到缓冲区无数据
                # 将接收缓冲区设的很小,
                # 用于测试LT和ET模式
                recv_data = client_socket.recv(4)
                if not recv_data:
                    # 获取套接字对应地址
                    print('对端关闭:', client_socket.getpeername())
                    client_socket.close()
                    self.epoll.unregister(fd)
                    self.fd_to_socket.pop(fd)
                    self.fd_to_buffer.pop(fd)
                    break
                buffer += recv_data
        except BlockingIOError:  # socket 设为非阻塞，缓存区无数据时读，会抛出这个异常
            self.epoll.modify(fd, select.EPOLLOUT | select.EPOLLET)
            self.fd_to_buffer[fd] = buffer

    def write_handler(self, fd):
        client_socket = self.fd_to_socket[fd]
        buffer = self.fd_to_buffer[fd]
        print(buffer.decode())
        client_socket.sendall(buffer.upper())
        self.epoll.modify(fd, select.EPOLLIN | select.EPOLLET)

    def close(self):
        for client_socket in self.fd_to_socket.values():
            client_socket.close()
        self.server_socket.close()
        self.epoll.close()


def main():
    address = ('localhost', 9527)
    max_events = 1  # 这个参数其实不关键，对 `listen` 和 `epoll` 基本没影响
    m = Manager(address, max_events)
    try:
        m.run()
    except KeyboardInterrupt:
        pass
    finally:
        m.close()
        print('关闭成功!')


if __name__ == '__main__':
    main()

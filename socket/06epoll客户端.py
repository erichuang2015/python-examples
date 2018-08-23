"""
一次 HTTP 请求，
select.EPOLLIN
触发貌似会分多次。
"""

import socket
import select


def main():
    epoll = select.epoll()

    sock = socket.socket()
    sock.setblocking(False)
    address = ('www.iceflow.club', 80)
    try:
        sock.connect(address)
    except BlockingIOError:  # socket 设置非阻塞后，第一次 connect 会抛出BlockingIOError
        pass
    # 和 connect 关联的事件是 OUT（发送事件）。
    epoll.register(sock.fileno(), select.EPOLLOUT | select.EPOLLET)

    while True:
        print('等待事件中...')
        events = epoll.poll()

        # 轮询注册的事件集合, 返回格式为[(文件句柄, 对应的事件), ...]
        for fd, event in events:
            print('fd: {}, event: {}'.format(fd, event))

            if event == select.EPOLLOUT:
                request = 'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: keep-alive\r\n\r\n'\
                    .format('/', 'www.iceflow.club')
                sock.send(request.encode())
                epoll.modify(fd, select.EPOLLIN | select.EPOLLET)

            elif event == select.EPOLLIN:
                buffer = b''
                try:
                    while True:
                        print('>>>读')
                        recv = sock.recv(1024)
                        if not recv:
                            sock.close()
                            exit(1)
                        buffer += recv
                except BlockingIOError:
                    print(buffer.decode())
                    print(len(buffer))
                    # epoll.unregister(sock.fileno())


if __name__ == '__main__':
    main()

import selectors
import socket


class Manager:

    def __init__(self):
        self.server_address = ('localhost', 9527)
        self.mysel = selectors.DefaultSelector()
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setblocking(False)
        self.server_sock.bind(self.server_address)
        self.server_sock.listen(32)
        self.mysel.register(self.server_sock, selectors.EVENT_READ, self.accept)

    def run(self):
        print('starting up on {} port {}'.format(*self.server_address))
        while True:
            print('waiting for I/O')
            for key, mask in self.mysel.select():
                callback = key.data
                callback(key.fileobj, mask)

    def read(self, connection, mask):
        """读取事件的回调"""

        client_address = connection.getpeername()
        print('read({})'.format(client_address))
        data = connection.recv(1024)
        if data:
            # 可读的客户端 socket 有数据
            print('>>>received {!r}'.format(data))
            connection.sendall(data)
        else:
            # 将空结果解释为关闭连接
            print('>>>closing')
            self.mysel.unregister(connection)
            connection.close()

    def accept(self, sock, mask):
        """有新连接的回调"""

        new_connection, addr = sock.accept()
        print('accept({})'.format(addr))
        new_connection.setblocking(False)
        self.mysel.register(new_connection, selectors.EVENT_READ, self.read)

    def close(self):
        self.server_sock.close()
        self.mysel.close()


def main():
    manager = Manager()
    try:
        manager.run()
    except KeyboardInterrupt:
        pass
    finally:
        manager.close()
    print('shutting down')


if __name__ == '__main__':
    main()

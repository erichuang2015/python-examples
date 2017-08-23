#!/usr/bin/env python3
# coding:utf-8

import socket


def fetch():
    sock = socket.socket()
    sock.connect(('baidu.com', 80))
    request = 'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n'
    sock.sendall(request.encode())
    response = b''
    while True:
        chunk = sock.recv(8192)
        response += chunk
        if not chunk:
            break
    headers, _, body = response.partition(b'\r\n\r\n')

    print('*'*60)
    print(headers.decode())
    print('*'*60)
    print(body.decode())
    print('*'*60)
    print(len(body))


if __name__ == '__main__':
    fetch()
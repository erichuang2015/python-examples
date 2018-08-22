#!/usr/bin/env python3
# coding: utf-8

"""原始http和https请求, 只支持默认端口."""

import socket
import ssl


def parse_url(url):
    """解析url.
    
    :param url: str, 去除协议后的url.

    :return host: str, 
            port: int,
            resource: str.
    """

    protocol, _, url = url.partition('://')
    protocol = protocol.lower()
    if protocol == 'http':
        port = 80
    elif protocol == 'https':
        port = 443
    else:
        raise SyntaxError

    try:
        pos = url.lower().index('/')
        host = url[:pos]
        resource = url[pos:]
        if (not resource.endswith('/')) and (resource.rfind('?') == -1):
            resource += '/'
    except ValueError:
        host = url
        resource = '/'

    return host, port, resource


def fetch(url):
    """发送请求.
    
    :param url: str, 请求的完整url.
    """

    host, port, resource = parse_url(url)

    sock = socket.socket()
    if port == 443:
        # 这种使用 ssl 方法，已经在 3.7 被标记为不推荐
        sock = ssl.wrap_socket(sock)

    sock.connect((host, port))
    request = 'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(resource, host)
    sock.sendall(request.encode())
    response = b''
    while True:
        chunk = sock.recv(8192)
        response += chunk
        if not chunk:
            break
    headers, _, body = response.partition(b'\r\n\r\n')

    # 默认进行utf-8解码
    print('*'*60)
    print(headers.decode())
    print('*'*60)
    print(body.decode())
    print('*'*60)
    print(len(body))


def main():
    url = 'https://www.baidu.com'
    fetch(url)


if __name__ == '__main__':
    main()

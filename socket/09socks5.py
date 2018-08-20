"""
socks5 流程。

1. 认证阶段：

  - 客户端发送格式：

    +----+----------+----------+
    |VER | NMETHODS | METHODS  |
    +----+----------+----------+
    | 1  |    1     |  1~255   |
    +----+----------+----------+

    - VER 字段是当前协议的版本号，也就是 5；

    - NMETHODS 字段是 METHODS 字段占用的字节数；

    - METHODS 字段的每一个字节表示一种认证方式，表示客户端支持的全部认证方式：

      0x00: NO AUTHENTICATION REQUIRED
      0x01: GSSAPI
      0x02: USERNAME/PASSWORD
      0x03: to X’7F’ IANA ASSIGNED
      0x80: to X’FE’ RESERVED FOR PRIVATE METHODS
      0xFF: NO ACCEPTABLE METHODS

  - 服务器返回格式：

    +----+--------+
    |VER | METHOD |
    +----+--------+
    | 1  |   1    |
    +----+--------+

    一般情况下服务端返回两种情况：
    0x05 0x00：告诉客户端采用无认证的方式建立连接；
    0x05 0xff：客户端的任意一种认证方式服务器都不支持。

  - 举个例子， 服务器无需认证的情况如下：

    client -> server: 0x05 0x01 0x00
    server -> client: 0x05 0x00


2. 连接阶段

  - 客户端发送格式：

    +----+-----+-------+------+----------+----------+
    |VER | CMD |  RSV  | ATYP | DST.ADDR | DST.PORT |
    +----+-----+-------+------+----------+----------+
    | 1  |  1  |   1   |  1   | Variable |    2     |
    +----+-----+-------+------+----------+----------+

    - CMD 字段 command 的缩写：

      0x01：CONNECT 建立 TCP 连接
      0x02: BIND 上报反向连接地址
      0x03：关联 UDP 请求

    - RSV 字段：保留字段，值为 0x00

    - ATYP 字段：address type 的缩写，取值为：
      0x01：IPv4
      0x03：域名
      0x04：IPv6

    - DST.ADDR 字段：destination address 的缩写，取值随 ATYP 变化：

      ATYP == 0x01：4 个字节的 IPv4 地址
      ATYP == 0x03：1 个字节表示域名长度，紧随其后的是对应的域名
      ATYP == 0x04：16 个字节的 IPv6 地址
      DST.PORT 字段：目的服务器的端口

  - 服务器返回格式：

    +----+-----+-------+------+----------+----------+
    |VER | REP |  RSV  | ATYP | BND.ADDR | BND.PORT |
    +----+-----+-------+------+----------+----------+
    | 1  |  1  |   1   |  1   | Variable |    2     |
    +----+-----+-------+------+----------+----------+

    - REP 字段

      0x00：succeeded
      0x01：general SOCKS server failure
      0x02：connection not allowed by ruleset
      0x03：Network unreachable
      0x04：Host unreachable
      0x05：Connection refused
      0x06：TTL expired
      0x07：Command not supported
      0x08：Address type not supported
      0x09：to 0xFF unassigned

  - 举个例子，客户端通过 127.0.0.1:8000 的代理发送请求：

    # request:        VER  CMD  RSV  ATYP DST.ADDR            DST.PORT
    client -> server: 0x05 0x01 0x00 0x01 0x7f 0x00 0x00 0x01 0x1f 0x40
    # response:       VER  REP  RSV  ATYP BND.ADDR            BND.PORT
    server -> client: 0x05 0x00 0x00 0x01 0x00 0x00 0x00 0x00 0x10 0x10

3. 传输阶段

  接下来就开始传输数据，socks5 服务器只做单纯的转发功能
"""

import logging
import socket
import struct
import select
import threading


def send_data(sock, data):
    print(data)
    bytes_sent = 0
    while True:
        r = sock.send(data[bytes_sent:])
        if r < 0:
            return r
        bytes_sent += r
        if bytes_sent == len(data):
            return bytes_sent


def handle_tcp(sock, remote):
    # 处理 client socket 和 remote socket 的数据流
    try:
        fdset = [sock, remote]
        while True:
            # 用 IO 多路复用 select 监听套接字是否有数据流
            r, w, e = select.select(fdset, [], [])
            if sock in r:
                data = sock.recv(4096)
                if len(data) <= 0:
                    break
                result = send_data(remote, data)
                if result < len(data):
                    raise Exception('failed to send all data')

            if remote in r:
                data = remote.recv(4096)
                if len(data) <= 0:
                    break
                result = send_data(sock, data)
                if result < len(data):
                    raise Exception('failed to send all data')
    except Exception as e:
        raise(e)
    finally:
        sock.close()
        remote.close()


def handle_con(sock, addr):
    # 接受客户端来的请求，socks5 的 认证和连接过程

    sock.recv(256)
    # 无需进一步认证信息
    sock.send(b"\x05\x00")
    data = sock.recv(4) or '\x00' * 4
    # CMD 为 0x01 也就是 CONNECT 继续
    mode = data[1]
    if mode != 1:
        return
    # DST.ADDR 有三种形式，分别做判断
    addr_type = data[3]
    if addr_type == 1:
        addr_ip = sock.recv(4)
        remote_addr = socket.inet_ntoa(addr_ip)
    elif addr_type == 3:
        addr_len = int.from_bytes(sock.recv(1), byteorder='big')
        remote_addr = sock.recv(addr_len)
    elif addr_type == 4:
        addr_ip = sock.recv(16)
        remote_addr = socket.inet_ntop(socket.AF_INET6, addr_ip)
    else:
        return
    # DST.PORT
    remote_addr_port = struct.unpack('>H', sock.recv(2))

    # 返回给客户端 success
    reply = b"\x05\x00\x00\x01"
    reply += socket.inet_aton('0.0.0.0') + struct.pack(">H", 8888)
    sock.send(reply)

    # 拿到 remote address 的信息后，建立连接
    try:
        # 连接到一个TCP服务监听网络地址address（host, port)，并返回一个socket对象。
        # 这是一个比socket.connect()高级的函数：
        # 如果是非IP地址，会尝试连接所有解析到的域名。与此同时兼容IPV6/4使得对客户端编程更容易
        remote = socket.create_connection((remote_addr, remote_addr_port[0]))
        logging.info('connecting %s:%d' % (remote_addr, remote_addr_port[0]))
    except socket.error as e:
        logging.error(e)
        return

    handle_tcp(sock, remote)


def main():
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socketServer.bind(('', 1080))
    socketServer.listen(5)

    print('已启动.')
    try:
        while True:
            print('等待连接中...')
            sock, addr = socketServer.accept()
            t = threading.Thread(target=handle_con, args=(sock, addr))
            t.start()
    except socket.error as e:
        logging.error(e)
    except KeyboardInterrupt:
        socketServer.close()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# coding: utf-8

import asyncio


async def wget(host):
    print('wget %s...' % host)
    reader, writer = await asyncio.open_connection(host, 80)
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        print('%s 跳过' % host)
        # 这里的 `readline()` 只会阻塞一次！
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


def main():
    host_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(wget(host)) for host in host_list]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()

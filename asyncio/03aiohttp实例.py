#!/usr/bin/env python3
# coding: utf-8

import asyncio

import uvloop
from aiohttp import ClientSession 

from finished import finished

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def wget(index, url, sem):
    # 限制最大并发数
    async with sem:
        async with ClientSession() as session:
            # 关闭Session是另一个异步操作，所以每次你都需要使用async with关键字
            async with session.get(url) as response:
                text = await response.text()
                print('%d: %s' % (index, text))


@finished
def main():
    url = 'http://127.0.0.1:5000/'

    # 限制并发数
    sem = asyncio.Semaphore(8)
    loop = asyncio.get_event_loop()
    # 发现 `loop.create_task()` 还能保证分组顺序
    # 分组内顺序不保证
    # tasks = [loop.create_task(wget(index, url, sem)) for index in range(16)]
    # 无序
    tasks = [wget(index, url, sem) for index in range(16)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()

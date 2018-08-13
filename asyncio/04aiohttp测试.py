#!/usr/bin/env python3
# coding: utf-8

import asyncio

from aiohttp import ClientSession 

from finished import finished


async def wget(index, url):
    # `ClientSession()` 必须放在 `async` 函数中
    session = ClientSession()
    response = await session.get(url)
    text = await response.text()
    print('%d: %s' % (index, text))
    await response.release()
    await session.close()


@finished
def main():
    url = 'http://127.0.0.1:5000/'

    loop = asyncio.get_event_loop()
    for i in range(8):
        tasks = [wget(index, url) for index in range(i*8+1, (i+1)*8+1)]
        loop.run_until_complete(asyncio.wait(tasks))
        print('%d轮结束' % (i + 1))
    loop.close()


if __name__ == '__main__':
    main()

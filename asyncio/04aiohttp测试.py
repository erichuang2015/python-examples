#!/usr/bin/env python3
# coding: utf-8

import asyncio
import uvloop

from aiohttp import ClientSession 

from finished import finished


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def wget(url):
    session = ClientSession()         
    response = await session.get(url)
    text = await response.text()
    await session.close()
    return text


@finished
def main():
    url = 'http://127.0.0.1:5000/'

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(wget(url)) for i in range(16)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    for task in tasks:
        print(task.result())


if __name__ == '__main__':
    main()

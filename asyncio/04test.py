#!/usr/bin/env python3
# coding: utf-8

import asyncio
import uvloop

from aiohttp import ClientSession 

from finished import finished


# 使用uvloop, 获得更高的事件循环速度
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def wget(url):
    # 关闭Session是另一个异步操作，所以每次你都需要使用async with关键字
    session = ClientSession()        
    response = await session.get(url)
    session.close()
    # return 和 await 可以连用,
    # return的结果不能直接获取,
    # 要先把coroutine封装成一个task,
    # 然后用result()方法获取
    text = await response.text()
    return text


@finished
def main():
    url = 'http://127.0.0.1:5000/'
    # 在未定义事件循环loop前,
    # 可以用asyncio.ensure_future()把coroutine封装成一个task,
    # task可以获取函数执行状态和返回值
    #tasks = [asyncio.ensure_future(wget(url)) for i in range(100)]

    loop = asyncio.get_event_loop()
    # 在定义事件循环loop后,
    # 可以用loop.create_task())把coroutine封装成一个task,
    tasks = [loop.create_task(wget(url)) for i in range(16)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    for task in tasks:
        # 获取函数返回结果
        print(task.result())


if __name__ == '__main__':
    main()

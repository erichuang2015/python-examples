#!/usr/bin/env python3
# coding: utf-8

import asyncio  # 引入asyncio 这个包，才可以使用 async 和 await
import threading


# 通过关键字async定义协程
# async定义的函数会变成一个无法直接执行的 coroutine 对象，必须将其注册到事件循环中才可以执行
async def hello(index):
    print('Hello world! index=%s, thread=%s' % (index, threading.currentThread().ident))
    # 模拟IO任务
    # await 用来挂起阻塞方法的执行
    # 只有async关键字定义的函数才能使用await
    await asyncio.sleep(1)
    print('Hello again! index=%s, thread=%s' % (index, threading.currentThread().ident))


def main():
    # 得到一个事件循环模型
    loop = asyncio.get_event_loop()
    # 初始化任务列表, hello()不会立即执行, 需放入事件循环中才行
    tasks = [hello(n) for n in range(8)]
    # 执行任务, 多个任务需要调用asyncio.wait(), 单个任务不需要
    loop.run_until_complete(asyncio.wait(tasks))    
    loop.close()

    
if __name__ == '__main__':
    main() 

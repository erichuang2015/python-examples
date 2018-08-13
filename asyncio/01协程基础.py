#!/usr/bin/env python3
# coding: utf-8

"""协程基础

整个程序都是单线程。

通过关键字 `async` 定义协程，
`async` 定义的函数会变成一个无法直接执行的 `coroutine` 对象，
必须将其注册到事件循环中才可以执行。

`await` 用来挂起阻塞方法的执行，
只有 `async` 关键字定义的函数才能使用 `await`。

一旦出现阻塞，异步函数就会切换到另一个函数执行，
直到任务列表中所有函数都执行一遍，
才会切回来继续执行剩下的内容。
所以，即使阻塞时间再短，一旦切换，
必须等待其他所有函数都执行一遍。
如果哦使用了 `Semaphore` 限制并发数，
那么会把并发数的任务量先执行完毕，
即分组执行。
但这里还有另一种情况：
切换后，发现另一个函数还在阻塞状态，
那么就会跳过它，直到整个任务列表都过一遍，
再重新执行自己剩下内容。
"""

import asyncio
import threading


async def func(index):
    print('sleep! index=%s, thread=%s' % (index, threading.currentThread().ident))
    # 模拟 IO 任务
    await asyncio.sleep(2)
    # 可以分开 `await`
    # s1p = asyncio.sleep(3)
    # await s1p
    # 异步函数返回值的方法和普通函数一样
    return 'sleep over! index=%s, thread=%s' % (index, threading.currentThread().ident)


async def hello(index):
        print('Hello world! index=%s, thread=%s' % (index, threading.currentThread().ident))
        # `await` 会进入函数，到达一个「异步点」时切换到另一个 `hello()` 执行
        s = await func(index)
        print(s)
        print('Hello again! index=%s, thread=%s' % (index, threading.currentThread().ident))
        # 在最外层 `async` 函数中，
        # `return` 的结果不能直接获取，
        # 要先把 `coroutine` 封装成一个 `task`，
        # 然后用 其`result()`方法获取
        return 'OK! %s' % index


def main():
    # 在未定义事件循环 `loop` 前，
    # 可以用 `asyncio.ensure_future()` 把 `coroutine `封装成一个 `task`。
    # tasks = [asyncio.ensure_future(hello(n)) for n in range(16)]

    # 得到一个事件循环模型，
    # 最外层的 `async` 函数必须放到 `loop` 中执行。
    loop = asyncio.get_event_loop()
    # 初始化任务列表，`hello()` 不会立即执行，需放入事件循环中才行

    # 在定义事件循环 `loop` 后，
    # 可以用 `loop.create_task()` 把 `coroutine` 封装成一个 `task`，
    # `task` 可以获取函数执行状态和返回值。
    # 注意任务列表不宜创建过大，因为是列表，会立即占用内存
    tasks = [loop.create_task(hello(n)) for n in range(8)]
    # 执行任务，多个任务必须需要调用 `asyncio.wait()`，
    # `asyncio.wait()` 本质也是一个异步函数，
    # 它包装一个列表
    loop.run_until_complete(asyncio.wait(tasks))    
    loop.close()
    for task in tasks:
        # 获取最外层异步函数的返回结果
        # **注意**：不太建议用这种方法获取函数结果，
        # 有可能导致内存爆掉，
        # 处理工作放在函数中进行即可。
        print(task.result())

    
if __name__ == '__main__':
    main() 

"""协程基础。

通过关键字 `async` 定义协程，
`async` 定义的函数会**返回**一个无法直接执行的 `coroutine` 对象，
必须将其注册到事件循环中才可以执行。

`await` 用来挂起阻塞方法的执行，
只有 `async` 关键字定义的函数才能使用 `await`。

一旦出现阻塞，异步函数就会切换到另一个函数执行，
直到任务列表中所有函数都执行一遍，
才会切回来继续执行剩下的内容。
所以，即使阻塞时间再短，一旦切换，
必须等待其他所有函数都执行一遍。
如果使用了 `Semaphore` 限制并发数，
那么会把并发数的任务量先执行完毕，
即分组执行。
但这里还有另一种情况：
切换后，发现另一个函数还在阻塞状态，
那么就会跳过它，直到整个任务列表都过一遍，
再重新执行自己剩下内容。

如果执行完阻塞任务，那么会一直往下执行（包括 `return` 出函数），
直到遇到另一个阻塞点，便再切换到另一个函数执行。
"""

import asyncio
import threading


async def func(index):
    print('sleep! index=%s, thread=%s' % (index, threading.currentThread().ident))
    # 模拟 IO 任务，阻塞点
    await asyncio.sleep(2)
    return 'sleep over! index=%s, thread=%s' % (index, threading.currentThread().ident)


async def hello(index):
    print('Hello world! index=%s, thread=%s' % (index, threading.currentThread().ident))
    # `await` 会进入函数，直到遇到一个「阻塞点」时切换到另一个 `hello()` 执行
    s = await func(index)
    print(s)
    print('Hello again! index=%s, thread=%s' % (index, threading.currentThread().ident))
    await asyncio.sleep(2)
    # 在最外层 `async` 函数中，
    # `return` 的结果不能直接获取，
    # 要先把 `coroutine` 封装成一个 `task`，
    # 然后用 其`result()`方法获取
    return 'OK! %s' % index


def main():
    # 得到一个事件循环模型，
    # 最外层的 `async` 函数必须放到 `loop` 中执行。
    loop = asyncio.get_event_loop()

    # `loop.create_task()` 把 `coroutine` 封装成 `task`
    task_list = [loop.create_task(hello(n)) for n in range(2)]

    try:
        # 执行列表多个任务必须调用 `asyncio.wait()`。
        done_set, pending_set = loop.run_until_complete(asyncio.wait(task_list))
        print(done_set)
        print(pending_set)
        for task in done_set:
            print(task.result())
    except KeyboardInterrupt:
        pass

    
if __name__ == '__main__':
    main() 

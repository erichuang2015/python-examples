"""协程与键盘中断。

探索如何正确退出协程，
目前还是没能找到一种合适的退出方式。

协程的接收键盘中断后的退出点，当前协程和其他协程要分别看待：
1. 当前协程
  - 处在 `await` 点：
    会直接退出，之后状态是 `pending`
  - 在执行任务，如下面的 `time.sleep(2)` 时：
    会直接退出，之后状态是 `done`, 会有 `exception=KeyboardInterrupt()`
2. 其他协程
  - 处在 `await` 点：
    会直接退出，之后状态是 `pending`
  - 处在执行任务：
    会继续往下执行，直到**所有**协程都到达下一个 `await` 点，才会响应键盘中断。
    之后状态是 `pending`

status：TODO
"""

import time
import asyncio

import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class Spider:

    def __init__(self):
        self._running = True
        self.loop = None
        self.db = []  # 存放数据
        self.task_list = None

    def run(self):
        self.loop = asyncio.get_event_loop()
        self.task_list = [self.loop.create_task(self.hello1(1)), self.loop.create_task(self.hello2(2))]
        #self.loop.run_until_complete(asyncio.wait(self.task_list))
        self.loop.run_forever()

    async def hello1(self, index):
        while self._running:
            print('hello1 %s' % index)
            await asyncio.sleep(2)
            self.save(index)
            print('over %s' % index)

    async def hello2(self, index):
        while self._running:
            print('hello2 %s' % index)
            await asyncio.sleep(2)
            self.save(index)
            print('over %s' % index)

    def save(self, index):
        print(index, 'save start')
        # 模拟存储耗时
        time.sleep(2)
        self.db.append(index)
        print(index, 'save end')

    def wait_complete(self):
        self._running = False
        # 返回所有存活协程
        for task in asyncio.Task.all_tasks(self.loop):
            print(task)
        print('*' * 30)
        for task in self.task_list:
            print(task)
        #self.loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(self.loop)))
        self.loop.stop()

    def close(self):
        self.loop.close()


def main():
    s = Spider()
    try:
        s.run()
    except KeyboardInterrupt:
        print("Caught keyboard interrupt. Canceling tasks...")
        s.wait_complete()
    s.close()
    print(s.db)


if __name__ == '__main__':
    main()

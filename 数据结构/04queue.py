"""Queue 常用于线程间共享数据，或作为任务队列。

Queue 可以设置阻塞或非阻塞（默认阻塞），
阻塞情况下，Queue 为空则阻塞等待。
非阻塞情况下， 为空则抛出 Empty 异常。
"""

from queue import Queue, Empty


def main():
    q = Queue()
    for i in range(10):
        q.put(i)

    while True:
        try:
            # 非阻塞
            i = q.get(block=False)
            # 或
            # i = q.get_nowait()
            print(i)
        except Empty:
            print('over')
            break


if __name__ == '__main__':
    main()
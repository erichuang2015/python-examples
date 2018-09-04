"""多进程爬虫通用框架，数据存储在 MongoDB 中。

任务分发，通过 Redis 或 multiprocessing.Queue() 来实现。
上锁通过 multiprocessing.Lock() 来实现。
"""

import os
import sys
import time
import multiprocessing

import requests
import pymongo
from redis import StrictRedis

CHILD_PROCESS_NUMBER = 2

# MongoDB
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DATABASE = 'database'  # mongodb 数据库名
MONGO_COLLECTION = 'collection'  # 存放爬取的数据

# Redis
REDIS_TASK_LIST = 'task_list'  # 读取任务


class Spider:

    headers = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0'
    }

    def __init__(self):
        self.mongo_conn = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        self.mongo_db = self.mongo_conn.get_database(MONGO_DATABASE)
        self.mongo_collection = self.mongo_db[MONGO_COLLECTION]  # 存放数据
        self.redis = StrictRedis()  # 读取数据

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def run(self):
        # TODO
        pass

    @staticmethod
    def parse(html):
        # TODO
        pass

    def save(self, item_list):
        for item in item_list:
            # 根据筛选条件id，更新这条记录
            # 如果找不到符合条件的记录，就插入这条记录（upsert=True）
            self.mongo_collection.update_one(
                filter={'id': item['id']},
                update={'$set': item},
                upsert=True
            )
        return True

    def close(self):
        self.session.close()
        self.mongo_conn.close()


def task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    s = Spider()
    try:  # 注意判断执行键盘中断时，代码在 try 内还是外面
        s.run()
    except:  # 子进程出现异常，屏幕不会打印出来，解决办法是捕获所有异常，并打印
        # 打印异常名
        t = str(sys.exc_info()[0])
        print(t)
        # 存储异常名
        with open('%s.txt' % os.getpid(), 'a') as f:
            f.write(t)
        print('Except ok!')
    finally:
        print('Enter finally!')
        s.close()
        print('Child process %s done.' % name)


def main():
    print('Parent process id is %s.' % os.getpid())
    p = multiprocessing.Pool(CHILD_PROCESS_NUMBER)
    for i in range(CHILD_PROCESS_NUMBER):
        p.apply_async(task, args=(i,))
    p.close()  # 调用 close() 之后就不能继续添加新的 Process 了

    print('Waiting for all subprocesses done...')
    t1 = time.time()
    try:
        p.join()  # join() 等待所有子进程结束
    except KeyboardInterrupt:  # 一次键盘中断，所有父子进程都会收到
        p.join()  # 这里必须再加个 join()，不然父进程有可能先结束
    t2 = time.time()
    print('\n[Finished in %.2fs]\n' % (t2 - t1))


if __name__ == '__main__':
    main()

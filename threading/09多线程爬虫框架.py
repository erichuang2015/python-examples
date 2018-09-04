"""多线程爬虫通用框架，数据存储在 MySQL 中。

任务分发，通过 Redis 或 threading.Queue() 来实现。
上锁通过 threading.Lock() 来实现。
"""

import atexit
import time
import threading

import requests
import pymysql

THREAD_NUM = 2

# MySQL
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'password'
MYSQL_DB = 'database'
MYSQL_TABLE_SAVE = 'table'


class Spider(threading.Thread):

    headers = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0'
    }

    insert_query_temp = 'INSERT INTO %s ({}) VALUES ({})' % MYSQL_TABLE_SAVE

    def __init__(self, name, daemon):
        super().__init__(name=name, daemon=daemon)

        atexit.register(self.close)  # 注册清理函数，线程结束时自动调用

        self._running = True

        self.mysql_conn = pymysql.connect(
            host=MYSQL_HOST, port=MYSQL_PORT,
            user=MYSQL_USER, password=MYSQL_PWD,
            db=MYSQL_DB, autocommit=True
        )
        self.cursor = self.mysql_conn.cursor()

        self.session = requests.Session()
        self.session.headers.update(self.headers)

        self.post_insert_query = None

    def run(self):
        print('%s 启动' % self.name)
        # TODO
        pass

    @staticmethod
    def parse(html):
        # TODO
        pass

    def save(self, item):
        if not self.post_insert_query:
            self.post_insert_query = self.insert_query_temp.format(
                ', '.join(item),
                ', '.join(f'%({k})s' for k in item)
            )
        try:
            self.cursor.execute(self.post_insert_query, item)
        except pymysql.IntegrityError:
            pass

    def terminate(self):
        self._running = False

    def close(self):
        self.session.close()
        self.cursor.close()
        self.mysql_conn.close()


def main():
    thread_list = []
    for i in range(THREAD_NUM):
        t = Spider(f'thread{i+1}', daemon=True)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    start = time.time()
    try:
        for t in thread_list:
            t.join()
    except KeyboardInterrupt:  # 只有主线程能收到键盘中断
        for t in thread_list:  # 防止下面在保存完 `row` 后，线程又请求一个新 `row`
            t.terminate()
    end = time.time()
    print('\n[Finished in %.2fs]\n' % (end - start))


if __name__ == '__main__':
    main()

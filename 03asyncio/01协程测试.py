#!/usr/bin/env python3
# coding:utf-8

import asyncio
import threading


# 通过关键字async定义协程
async def hello(index):       
    print('Hello world! index=%s, thread=%s' % (index, threading.currentThread()))
    # 模拟IO任务
    await asyncio.sleep(1)     
    print('Hello again! index=%s, thread=%s' % (index, threading.currentThread()))


def main():
    # 得到一个事件循环模型
    loop = asyncio.get_event_loop() 
    # 初始化任务列表    
    tasks = [hello(n) for n in range(8)]
    # 执行任务
    loop.run_until_complete(asyncio.wait(tasks))    
    loop.close() 

    
if __name__ == '__main__':
    main() 

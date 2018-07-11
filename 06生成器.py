#!/usr/bin/env python3
# coding: utf-8

"""生成器演示生产者, 消费者例子."""


def consumer():
    """定义消费者，由于有yeild关键词，此消费者为一个生成器."""

    print('[Consumer] Init Consumer ......')
    r = 'init OK'
    while True:
        n = yield r 
        print('[Consumer] conusme n = %d, r = %s' % (n, r))
        r = 'consume %s OK' % n


def producer(c):
    """定义生产者."""

    print('[Producer] Init Producer ......')
    r = next(c)         # 启动消费者生成器, 同时第一次接收返回结果
    # r = consumer.send(None)  # 等同于next, 第一次启动, 参数应该为None
    print('[Producer] Start Consumer, return %s' % r)
    for n in range(1, 6):
        print('[Producer] While, Producing %d ......' % n)
        r = c.send(n)   # 向消费者发送消息, 同时准备接收结果, 此时会切换到消费者执行
        print('[Producer] Consumer return: %s' % r)
    c.close()           # 关闭消费者生成器
    print('[Producer] Close Producer ......')


if __name__ == '__main__':
    producer(consumer())

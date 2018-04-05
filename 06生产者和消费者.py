#!/usr/bin/env python3
# coding:utf-8

"""生产者, 消费者例子."""


def consumer():         # 定义消费者，由于有yeild关键词，此消费者为一个生成器
    print("[Consumer] Init Consumer ......")
    r = "init ok"       # 初始化返回结果，并在启动消费者时，返回给生产者
    while True:
        n = yield r     # 消费者通过yield关键词接收生产者产生的消息，同时返回结果给生产者
        print("[Consumer] conusme n = %s, r = %s" % (n, r))
        r = "consume %s OK" % n     # 消费者消费结果，下个循环返回给生产者


def produce(c):         # 定义生产者，此时的 c 为一个生成器
    print("[Producer] Init Producer ......")
    r = next(c)         # 启动消费者生成器，同时第一次接收返回结果
    # r = c.send(None)  # 等同于next，第一次启动参数应该为None
    print("[Producer] Start Consumer, return %s" % r)
    for n in range(1, 6):
        print("[Producer] While, Producing %s ......" % n)
        r = c.send(n)   # 向消费者发送消息，同时准备接收结果。此时会切换到消费者执行
        print("[Producer] Consumer return: %s" % r)
    c.close()           # 关闭消费者生成器
    print("[Producer] Close Producer ......")


if __name__ == '__main__':
    produce(consumer())

"""
来看 x = yield i 这个表达式如果这个表达式只是x = i, 
相信每个人都能理解是把i的值赋值给了x(虽然python是引用,不过不碍事), 
而现在等号右边是一个yield i,所以先要执行yield i,
然后才是赋值yield把i值返回到了调用者那里这个表达式的下一步操作:
赋值却因为等号右边的yield被暂停了,
换句话说x = yield i才执行了一半,
当调用者通过send(var)回到生成器函数时是回到之前那个赋值表达式被暂停的那里,
所以接下来执行x = yield i的另一半,
那就是这个赋值操作啦这个值正是调用者通过send(var)发送进生成器的值然后被打印,
然后循环下一次执行,然后又来到yield i,然后又暂停,重复以上描述
"""
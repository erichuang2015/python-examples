"""本地线程对象。

在多线程环境下，每个线程都有自己的数据。
一个线程使用自己的局部变量比使用全局变量好，
因为局部变量只有线程自己能看见，不会影响其他线程，
而全局变量的修改必须加锁。

但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦。
如果用一个全局dict存放所有的Student对象，
然后以thread自身作为key获得线程对应的Student对象的话,
代码会比较丑。

可以用threaing的Local类解决这个问题。
"""

import threading


# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

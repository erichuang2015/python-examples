"""信号实验

经过测试，绝大部分信号会直接终止程序，
程序不会执行 except 和 finally 内容。

除外情况（目前发现）：
`signal.SIGINT`  由 Ctrl + c 按出。
"""

import signal
import os
import time
import atexit


def p():
    print(123)


def task(name):
    # 注册回调函数，程序结束时调用
    # 感觉和 finally 一个意思
    # finally 会执行的，它也会执行
    # finally 不会执行的，它也不会执行
    atexit.register(p)

    print('start task %s' % name)

    # alarm 不会触发异常和 finally
    signal.alarm(3)

    # 效果同上，但立即触发
    # os.kill(os.getpid(), signal.SIGALRM)

    # 告诉程序正常结束，也不会触发异常和 finally
    # os.kill(os.getpid(), signal.SIGTERM)

    # 会触发异常和 finally
    os.kill(os.getpid(), signal.SIGINT)
    
    time.sleep(4)
    print('task over!')


def main():
    try:
        task(1)
    except:
        print('except!')
    finally:
        print('finally!')


if __name__ == '__main__':
    main()

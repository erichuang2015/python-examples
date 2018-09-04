"""信号实验

经过测试，绝大部分信号会直接终止程序，
程序不会执行 except 和 finally 内容。
但可以捕获信号，使程序正常退出。

除外情况（目前发现）：
`signal.SIGINT`  由 Ctrl + c 按出。
"""

import signal
import os
import time


def signal_handler(signum, frame):
    print('I received: ', signum, frame)
    exit(1)


def task(name):
    # 注册信号处理函数，改变原本信号的行为
    signal.signal(signal.SIGALRM, signal_handler)

    print('start task %s' % name)

    # alarm 不会触发异常和 finally
    signal.alarm(3)

    # 效果同上，但立即触发
    # os.kill(os.getpid(), signal.SIGALRM)

    # 告诉程序正常结束，也不会触发异常和 finally
    # os.kill(os.getpid(), signal.SIGTERM)

    # 会触发异常和 finally
    # os.kill(os.getpid(), signal.SIGINT)
    
    time.sleep(4)
    print('task over!')


def main():
    try:
        task(1)
    except KeyboardInterrupt:
        print('except!')
    finally:
        print('finally!')


if __name__ == '__main__':
    main()

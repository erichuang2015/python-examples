"""实现守护进程"""

import sys
import os
import time
import fcntl
import signal
import atexit
import argparse


class Daemon:
    """
    通用的Daemonlize类，能将一个程序变成守护进程
    使用方式：继承Daemon类，然后重写run()函数即可
    """

    def __init__(self, pidfile='/home/zzzzer/nbMon.pid', stdin='/dev/null', stdout='/home/zzzzer/log.log', stderr='/home/zzzzer/log.log'):
        # 其实 pidfile 一般放在 /var/run 中，log 一般放在 /var/log 中，
        # 但要 root 权限
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

        self.pf = None

    def daemonize(self):

        # 创建子进程，父进程退出
        try:
            pid = os.fork()
            if pid > 0:
                exit(0)
        except OSError as e:
            sys.stderr.write('fork failed: %d (%s)\n' % (e.errno, e.strerror))
            exit(1)

        # 捕获 TERM 信号，
        # 原版的 TERM 信号，会使程序直接退出，
        # 没法进行清理工作。
        def signal_handler(signum, frame):
            exit(0)

        signal.signal(signal.SIGTERM, signal_handler)

        # 需要执行一些操作避免可能从父进程继承过来的影响守护进程的设定
        # 改变当前工作目录
        os.chdir('/')

        # 重设umask
        os.umask(0)

        # 设置sid，成为session Leader
        os.setsid()

        # 重定向0、1、2三个fd（依次为标准输入、标准输出、错误输出）
        # 这里需要注意，有些不讲究的程序或者文章，会直接将0、1、2关闭，
        # 这样会造成一定的隐患，可能会导致后续操作打开的文件句柄占用
        # 0、1、2这三个一般认为有特殊含义的句柄，会导致一些莫名其妙的问题发生
        # 所以这里最好的建议是，将这三个fd重新定向到/dev/null,或者相应的日志文件
        # 重新定向之前flush一次，确保该打印出来的文字已经输出
        sys.stdout.flush()
        sys.stderr.flush()
        mysi = open(self.stdin, 'r')
        myso = open(self.stdout, 'a')
        myse = open(self.stderr, 'a', 1)  # 1代表一行行写入，只能用于文本模式
        os.dup2(mysi.fileno(), sys.stdin.fileno())
        os.dup2(myso.fileno(), sys.stdout.fileno())
        os.dup2(myse.fileno(), sys.stderr.fileno())

        # 注册一个函数，在程序结束前会被执行
        atexit.register(self.del_pidfile)
        pid = os.getpid()
        # 这里 open() 不能赋值给局部变量，用完会被释放掉，锁也就没了
        self.pf = open(self.pidfile, 'w')
        fcntl.flock(self.pf.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        self.pf.write('%s\n' % pid)
        self.pf.flush()

    def del_pidfile(self):
        os.remove(self.pidfile)

    def start(self):
        """启动守护进程"""

        # 用于判断守护进程是否已经在运行，实现单例模式。
        # 如果pid文件文件上锁失败，则认为守护进程还在运行
        try:
            with open(self.pidfile) as f:
                fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except FileNotFoundError:  # 说明当前没有相关守护进程运行，跳过
            pass
        except BlockingIOError:  # 上锁失败
            sys.stderr.write('pidfile %s already exist. Daemon already running?\n' % self.pidfile)
            exit(1)

        self.daemonize()
        self.run()

    def stop(self):
        """停止守护进程"""

        # 从pid文件中获取进程id
        pid = None
        try:
            with open(self.pidfile, 'r') as pf:
                pid = int(pf.read().strip())
        except FileNotFoundError:
            pass

        if not pid:
            message = 'pidfile %s does not exist. Daemon not running?\n'
            sys.stderr.write(message % self.pidfile)
            exit(1)

        # 直到杀死为止
        # 必须确保程序被杀死，
        # 因为信号必须等程序执行到某个节点，才能执行
        # 这时 restart 时，start 可能会在 pid 尚未移除前执行
        try:
            while True:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except ProcessLookupError:
            pass

    def restart(self):
        """重启守护进程"""

        self.stop()
        self.start()

    def run(self):
        """
        这个方法是空的，所以要想使用这个类，必须在子类中
        重写这个函数，这个函数应该写的是程序的主逻辑循环。
        后面这个函数将会在start()和restart()函数中被调用。
        """

        raise NotImplementedError


def arg_parse():
    """添加命令行参数"""

    parser = argparse.ArgumentParser(description='A Daemon.')

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s v0.1'
    )
    # 实现不需要指定值的参数功能
    # 不指定时, 该值默认是False, 所以不用再设置default参数
    parser.add_argument(
        '-d',
        dest='daemon',
        choices=['start', 'stop', 'restart'],
        help='whether daemon'
    )
    return parser.parse_args()


if __name__ == '__main__':
    class Test(Daemon):
        def run(self):
            while True:
                sys.stdout.write('hello\n')
                time.sleep(5)

    t = Test()

    p = arg_parse()
    if p.daemon == 'start':
        t.start()
    elif p.daemon == 'stop':
        t.stop()
    elif p.daemon == 'restart':
        t.restart()

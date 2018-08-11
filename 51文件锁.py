"""利用文件锁实现，同一时刻，
某文件只能被一个进程打开，
可以用在守护进程中，
实现单例守护进程。

运行该脚本两次，看见效果

注意：
1. 对于文件的 close() 操作会使文件锁失效；
2. 同理，进程结束后文件锁失效；
3. flock() 的 LOCK_EX是「劝告锁」，系统内核不会强制检查锁的状态，
   需要在代码中进行文件操作的地方显式检查（即用 fcntl.flock() 检查）才能生效。
"""

import time
import fcntl
import sys


f = open('00test.py', 'r')
try:
    # LOCK_NB 代表不阻塞，默认情况下，
    # LOCK_EX 模式下的 flock() 会阻塞等待。
    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError as e:
    sys.stderr.write('flock failed: %d (%s)\n' % (e.errno, e.strerror))
time.sleep(10)
f.close()

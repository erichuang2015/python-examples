"""在 python 中执行其他 python 文件。"""

import os
import time


os.system('python 01Python之禅.py')
# 可以看到是同步的
time.sleep(2)
print('over')
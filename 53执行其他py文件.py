"""在 python 中执行其他 python 文件。"""

import os
import time
import subprocess


# os.system('python 01Python之禅.py')
subprocess.call(['python', '35urllib使用.py'])
print('over')

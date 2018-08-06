"""
注意不同时间类型不能相互比较,
如datetime.date类和datetime.datetime类.
"""

import time
import datetime


# 今天日期
d = datetime.date.today()
print(d)
print('*' * 50)

# 今天日期和时间
dt = datetime.datetime.today()
print(dt)
print('*' * 50)

# 今天零点时间
dt = datetime.datetime(d.year, d.month, d.day)
print(dt)
print('*' * 50)

# 转换为标准时间
s = '2017年7月20日 10点25分10秒'
dt = datetime.datetime.strptime(s, '%Y年%m月%d日 %H点%M分%S秒')
print(dt)
print(dt.strftime('%Y-%m-%d'))
print('*' * 50)

# 生成unix时间戳
t = time.time()
print(t)
timestamp = int(t) # 保留精度秒
print(timestamp)
print('*' * 50)

# 时间戳转换成时间, 可存入mysql(DATETIME类型)
dt = datetime.datetime.fromtimestamp(timestamp)
print(dt)
print('*' * 50)

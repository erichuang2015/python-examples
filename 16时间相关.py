#!/usr/bin/env python3
# coding: utf-8

import datetime


# 今天日期
d = datetime.date.today()
print(d)

# 今天日期时间
dt = datetime.datetime.today()
print(dt)

# 转换为标准时间
s = '2017年7月20日 10点25分10秒'
dt = datetime.datetime.strptime(s, '%Y年%m月%d日 %H点%M分%S秒')
print(dt)
print(dt.strftime('%Y-%m-%d'))

# 生成unix时间戳, 精度秒
import time
t = time.time()
print(t)
timestamp = int(t)
print(timestamp)
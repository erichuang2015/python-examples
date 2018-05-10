#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime


s = '2017年7月20日 10点25分10秒'
dt = datetime.strptime(s, '%Y年%m月%d日 %H点%M分%S秒')
print(dt)
print(dt.strftime('%Y-%m-%d'))

# python提供了一个time和calendar模块用于格式化日期和时间
# 时间间隔是秒为单位的浮点小数,时间搓适合做日期运算

import time

ticks=time.time()
# 获取当前时间
localtime=time.localtime(time.time())
print("the time is:",ticks)
print("local time:",localtime)
# python提供了一个time和calendar模块用于格式化日期和时间
# 时间间隔是秒为单位的浮点小数,时间搓适合做日期运算

import time
import calendar

ticks=time.time()
# 获取当前时间
localtime=time.localtime(time.time())
print("the time is:",ticks)
print("local time:",localtime)
# time.struct_time(tm_year=2019, tm_mon=4, tm_mday=5, tm_hour=21, tm_min=10, tm_sec=20, tm_wday=4, tm_yday=95, tm_isdst=0)

# 获取格式化时间
localtime1=time.asctime(time.localtime(time.time()))
print("the local time is :",localtime1)

# 获取格式化日期
print(time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime()))
# 2019-04-05  21:17:31
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))
# Fri Apr 05 21:17:31 2019

cal=calendar.month(2016,2)
print("输出2016年1月份的日历：",cal)
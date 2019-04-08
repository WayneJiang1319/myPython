# python提供了一个time和calendar模块用于格式化日期和时间
# 时间间隔是秒为单位的浮点小数,时间搓适合做日期运算

import time
import calendar

ticks=time.time()# 时间搓，适合做日期运算
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

# python获取系统时间
print(time.perf_counter())# 返回系统运行时间
print(time.process_time())# 返回进程运行时间

# python推迟调用线程的运行时间，secs指秒数
print("start time:%s" % time.ctime())
time.sleep(0.1)
print("end time:%s" % time.ctime())

# calendar模块中：星期一时是默认的每周第一天，星期天是默认的最后一天。更改设置可调用calendar.setFirstWeekDay()函数

# 判断是否为闰年
print(calendar.isleap(2000))
print(calendar.isleap(1900))
# calendar.leapdays(y1,y2) 判断y1和y2之间所有的闰年
print(calendar.leapdays(1900,2000))

# calendar.monthrange(year,month)
print(calendar.monthrange(2014,11))
# (5,30) 5表示2014年的11月份的第一天是周六，30表示2014年的11月份总共有30天



# python中线程模块为_thread
# python中使用线程有两种方式：函数或者类来包装线程对象
# 产生线程的方法：
# _thread.start_new_thread(function,args[,kwargs])
# function为线程函数、args为线程函数的参数，而且必须为tuple类型
# kwargs为可选参数


import _thread
import  time
# 线程定义一个函数
def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count +=1
        print("%s:%s" %(threadName,time.ctime(time.time())))

# 创建两个线程

try:
    _thread.start_new_thread(print_time,("Thread-1",2,))
    _thread.start_new_thread(print_time,("Thread-2",4,))

except:
    print("Error:无法启动线程")

while 1:
    pass



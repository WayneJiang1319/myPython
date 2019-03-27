# python中线程模块为_thread
# python中使用线程有两种方式：函数或者类来包装线程对象
# 产生线程的方法：
# _thread.start_new_thread(function,args[,kwargs])
# function为线程函数、args为线程函数的参数，而且必须为tuple类型
# kwargs为可选参数

#
# import _thread
# import  time
# # 线程定义一个函数
# def print_time(threadName,delay):
#     count=0
#     while count<5:
#         time.sleep(delay)
#         count +=1
#         print("%s:%s" %(threadName,time.ctime(time.time())))
#
# # 创建两个线程
#
# try:
#     _thread.start_new_thread(print_time,("Thread-1",2,))
#     _thread.start_new_thread(print_time,("Thread-2",4,))
#
# except:
#     print("Error:无法启动线程")
#
# while 1:
#     pass

# 使用threading模块创建线程

# python中threading和_thread都可以提供线程的支持
# _thread提供了低级别、原始的线程和一个简单锁，相比threading功能还是有限的
# threading模块中包含了_thread模块，还提供其他方法
# threading.currentThread():返回当前线程的线程变量
# threading.enumerate():返回一个包含正在运行的线程list。正在运行指线程启动后、结束前、不包括启动前和终止后的线程
# threading.activeCount():返回正在运行的线程数量，与len(threading.enumberrate())有相同的结果
# 常见方法：run()：用以表示线程活动的方法
# start()：启动线程活动
# join([time]):等待至线程中止。这阻塞调用线程直至线程的join()方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
# isAlive()：返回线程是否是活动的
# getName()：返回线程名
# setName()：设置线程名
import threading
import time

exitFlag=0

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter
    def run(self):
        print("开始线程："+self.name)
        print_time(self.name,self.counter,5)
        print("退出线程："+self.name)

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s"%(threadName,time.ctime(time.time())))
        counter -=1


thread1=myThread(1,"Thread-1",1) # ID=1;name="Thread-1";counter=1
thread2=myThread(2,"Thread-2",2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
# 运行结果
# 开始线程：Thread-1
# 开始线程：Thread-2
# Thread-1:Thu Mar 28 06:48:25 2019
# Thread-2:Thu Mar 28 06:48:26 2019
# Thread-1:Thu Mar 28 06:48:26 2019
# Thread-1:Thu Mar 28 06:48:27 2019
# Thread-2:Thu Mar 28 06:48:28 2019
# Thread-1:Thu Mar 28 06:48:28 2019
# Thread-1:Thu Mar 28 06:48:29 2019
# 退出线程：Thread-1
# Thread-2:Thu Mar 28 06:48:30 2019
# Thread-2:Thu Mar 28 06:48:32 2019
# Thread-2:Thu Mar 28 06:48:34 2019
# 退出线程：Thread-2
# 退出主线程


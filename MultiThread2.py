# 线程同步：使用thread对象的lock和rclock可以实现线程同步，这两个对象都有acquire方法和release方法。一个是给线程加锁，另外一个释放锁

import threading
import time

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("start thread:"+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s:%s" %(threadName,time.ctime(time.time())))
        counter-=1

# 创建线程锁
threadLock = threading.Lock()
# 定义一个线程list
threads=[]
# 两个线程实例thread1和thread2
thread1=myThread(1,"Thread-1",1)
thread2=myThread(2,"Thread-2",2)

# 启动线程1和线程2
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("exit the main thread!")







# python语法的两种常见错误

# 语法错误，指python解析错误
# while True:
#     print("hello world")

# 异常：
# print(10/0)

# # 异常处理
# while True:
#     try:
#         x=int(input("please enter a number:"))
#         break
#     except ValueError:
#         print("Oops! there is no valid number,try again")

# 一个try语句可能包含多个except子句，分别处理不同的异常，但是最多只有一个分支会被执行。处理程序只针对对应的try字句总的异常进行处理
# 一个except也可以同时处理多个异常，这些异常将被放到一个括号里组成一个元组
# except(RuntimeError,TypeError,NameError)# nameError可以的当做通配符使用，可以使用这个方法打印一个错误的信息，然后再次将异常抛出

import sys

try:
    f=open('file.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("could not convert data to interger")
except:
    print("Unexpected error",sys.exc_info(0))
    raise

for arg in sys.argv[1:]:
    try:
        f=open(arg,'r')
    except IOError:
        print("Can not open",arg)
    else: # else 字句必须放到所有except字句后执行，这个字句将在try字句没有发生任何异常的时候执行
        print(arg,'has',len(f.readlines()),'lines')
        f.close()

# 抛出异常 raise

# # raise NameError('HiThere')  raise唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者异常类
# try:
#     raise NameError('Hi There')
# except NameError:
#     print("An exception flew by!")
#     raise

# 用户自定义异常：可以创建一个新的异常类来拥有自己的异常，异常类继承自Exception类，可以直接继承，或者间接继承

class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print("my exception occured ,value",e.value)

# 定义清理行为 try语句中还有另外一个可选的finally子句，定义了无论在任何情况下都会执行的清理行为
# 如果一个异常在try字句里面被抛出，但是又没有任何except把它截住，那么这个异常会在finally子句执行后再次被抛出
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by Zero")
    else:
        print("Result is ",result)
    finally:# 无论怎么样，这个finally子句都会被执行
        print("Executing finally clause")

print(divide('2',0))

# 预定义的清理行为 with语句！！


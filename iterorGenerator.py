# 迭代是一个记住遍历的位置的对象
# 迭代器对象可以从集合的第一个元素访问，知道所有元素被访问完毕，只会往前，不会后退
# 迭代器两个基本方法：iter() and next()
# string,list,tuple都可以创建迭代器
list=[1,2,3,4]
it = iter(list) #create a iteration  iter1=iter(???)
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))

for x in it:
    print(x, end=" ")

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x = self.a
        self.a+=1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# 把一个类作为迭代器需要在类中实现两个方法_iter_() 与_next_()
# _iter_()方法返回一个特殊的迭代器对象，这个迭代器对象实现了_next_()方法并通过StopIteration异常标志迭代的完成
# _next_()方法会返回下一个迭代器对象
# StopIteration异常用于标识迭代的完成，防止出现无限循环的情况。可以在_next_()方法中设置完成的指定循环次数后触发StopIteration

class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=mynumbers()
myiter=iter(myclass)

for x in myiter:
    print(x)

# 使用yield函数被称为生成器generator
# 生成器是一个返回迭代器的函数，只能用于迭代操作，生成器就是一个迭代器
# 调用一个生成器函数，返回的就是一个迭代器对象

import sys

def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
           return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)

while True:
    try:
        print(next(f),end='')
    except StopIteration:
        sys.exit()
# python输出方式：表达式语句，print()函数
# 输出使用文件对象的write()方法，标准文件输出可以使用sys.stdout
# 如果希望输出的形式更加多样，可以用str.format()韩式格式化输出值
# 如果希望将输出的值转成字符串，可以使用repr()和str()函数来实现：
# str() 返回用户一个容易读的表达形式
# repr() 产生一个解释器易读的表达形式
s='Hello, Runoob'
print(str(s)) # 用户容易读
print(repr(s))# 解释器容易读
print(str(1/7))

# 两种方式输出一个平方与立方的表
for x in range(1,3):
    print(repr(x),repr(x*x),end=' ')
# 输出：1 1 2 4
# end=''输出不换行的，end=' ' 与end='  '是不一样的

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3))
    #print(repr(x*x*x).rjust(4))
# 字符串rjust()方法表示在输出字符串时靠右边，并在左边填充空格

# zfill会在数字的左边填充0
print('12'.zfill(5))
# output:00012


# str.format()方法
print('{}网址："{}!"'.format('cainiao','www.runoob.com'))
print('{0} and {1}'.format('Google','Runoob'))

print('{1} and {0}'.format('Google','Runoob'))


# '!a' 使用ascii()方法，'!S'使用str()方法，'!r'使用repr()方法用于格式化某个值之前进行转化
import  math

print('常量pi的值为：{}。'.format(math.pi))
print('常量PI的值为：{!r}。'.format(math.pi))
print('常量PI的值近似为{0:.3f}'.format(math.pi))

# python 读取键盘输入input
# str=input("Please input:");
# print("你输入的内容是",str)

# 读和写文件 open()将会返回一个file对象。基本语法格式如下：
#open(filename,mode)

f=open("C:\\JW-workspace\\gitplace_python\\myPython\\foo.txt","w")
# 第一个参数为需要打开的文件名，注意windows下面是双斜杠。第二个参数描述文件如何使用字符
# r是只读，如果mode不指定，则默认为r。w是只写（存在同名文件则被删除），a用于追加内容，所写内容都会被自动追加到末尾，r+同时用于读写。
f.write("python is a good program language.\n yes,you are right!\n")
f.close()



f=open("C:\\JW-workspace\\gitplace_python\\myPython\\foo.txt","r")
# f.read() 读取一定数目的数据，然后作为字符串或者字节对象返回。size是一个可选的数字类型参数，当size被忽略或者为负
# 那么该文件所有内容都将被读取并且返回
str=f.read()
print(str)
f.close()

f=open("C:\\JW-workspace\\gitplace_python\\myPython\\foo.txt","r")
# f.readline()会从文件中单独读取一行，换行符为'\n',f.readline()如果返回一个空字符串，那么说明已经读取到最后一行了
str=f.readline()
print(str)
f.close()

f=open("C:\\JW-workspace\\gitplace_python\\myPython\\foo.txt","r")
str=f.readlines()
print(str)
f.close()

# 循环读取
f=open("C:\\JW-workspace\\gitplace_python\\myPython\\foo.txt","r")
for line in f:
    print(line,end=' ')
f.close()

# f.tell() 返回文件对象当前所处的位置，它是从文件开头开始算起的字节数

# f.seek()????干啥用的 改变文件当前的位置，可以使用f.seek(offset,from_what)函数
# seek(x,0):从起始位置即文件首行首字符开始移动x个字符
# seek(x,1)：从文件当前文职往移动x个字符
# seek(-x,2):表示从文件结尾往前移动x个字符
f=open("C:\\JW-workspace\\gitplace_python\\myPython\\file.txt","rb+")
f.write(b'0123456789abcdef')
print(f.seek(5))

print(f.read(1))

print(f.seek(-3,2))

# f.close()当处理完毕后，调用f.close()来关闭文件并释放系统的资源。


# pickle模块：实现数据的序列和发序列化
# 通过pickle模块的反序列化操作我们可以将程序中运行的对象信息保存到文件中，永久储存
# 通过pickle模块的反序列化操作，我们能从文件中创建上一次程序保存的对象

import pickle

data1={'a':[1,2.0,3,4+6j],'b':('string',u'unicode string'),'c':None}

selfref_list = [1,2,3]
selfref_list.append(selfref_list)

output=open('data.pkl','wb')

pickle.dump(data1,output)
# 序列化对象：pickle.dump(obj,file,[protocol])
# 反序列化对象：pickel.load(file)
pickle.dump(selfref_list,output,-1)

output.close()


import pprint,pickle

pkl_file = open('data.pkl','rb')

data1=pickle.load(pkl_file)
pprint.pprint(data1)

data2=pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()


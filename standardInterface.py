# 操作系统接口
import os
os.getcwd()
print(os.getcwd())

print(dir(os))
print(help(os))


# 文件通配符
import  glob

glob.glob('*.py')
# print(glob.glob('*.py'))

print(glob.glob('*.txt'))


# 命令行参数 sys

import  sys

print(sys.argv)

# 错误输出重定向和程序终止
# stdin,stdout,stderr
# 脚本的定向终止使用sys.exit()

# 字符串正则匹配

import re

print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+)\ 1',r'\1','cat in the the cat'))

print(re.findall(r'\bw[a-z]*','which foot or hand fell fastest'))

print('tea or too'.replace('too','two'))

# math模块

import math
print (math.cos(math.pi/4))

# random模块提供了生成随机数的工具
import random

print(random.choice(['apple','pear','banana']))
print(random.random())
print(random.randrange(6))

# 访问互联网、处理网络通信协议，最简单的是处理从urls接收的urlib.request以及用于发送电子邮件的smtplib:

# 日期和时间 datetime
from datetime import date

now=date.today()
print(now)

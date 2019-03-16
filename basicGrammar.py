print('--------------------------------------------------------')


print('i am leraning python')
# this is my python testing code
print("i am learning \n python")
# python has three kinds of annotations

# 1.python注意必须缩进一致
if True:
    print('TRUE')
else:
    print('False')

# 多行语句：如果语句很长，可以使用反斜杠来实现多行语句

# python中数字有四种类型，分别为整数、布尔型、浮点数和复数
# int整数：python只有int，没有long
# bool 布尔，比如true
# float浮点数
# complex复数



#-*-coding:utf-8-*-
# 字符串学习
# python中单引号和双引号的使用完全相同
# 使用三引号可以指定一个多行字符串
# 转义符‘\’
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
# 按照字面串联，字符串可以通过+运行符连接在一起，用*是重复
# python中的字符窜有两种索引方式，从左到右以0开始，从右往左从-1开始
# python中字符串不能被改变
# python中没有单独的字符类型，一个字符就是长度为1的字符串
# python中截取的语法的格式：变量[头下标：尾下标：步长]

str="Runoob"
print(str)
print(str[0:-1])# 表示截取从第一个到倒数第二个字母之间的字符串
print(str[0])
print(str[-1])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+'您好')

print('------------------------------------------------------')

print('hello \nrunnoob')# \n换行符
print(r'hello\nrunoob')# r表示还安装原来的字符

# 空行学习
# 空行也是代码的一部分，但是作用主要是在于分离两端功能不同的代码

print('--------------------------------------------------------')
#同一行显示多条语句
# the same line can have two or more code line,but it needs to be sepreated by ';'.
import sys;x= 'runoob';sys.stdout.write(x + '\n')

print('---------------------------------------------------------')

# 代码组:缩进相同的一组语句构成一个代码块，称为代码组
# if while else 等组成的复合语句，首行以关键字开始，以冒号(:)结束
expression1=4>5
expression2=4<5

if expression1:
    print('This is False!')
elif expression2:
    print('This is True!')
else:
    print('I do not know!')

print('----------------------------------------------------------')

# import 与from... import
# 将整个模块somemodule导入，格式为：import somemoudle
# 将某个模块中导入某个函数，格式为：from somemodule import some function
# 从某个模块中导入多个函数：from module improt function1,function2,function3
# 将某个模块中的全部函数导入：frome module import *

import sys
print('================Python import mode ========================')
print('the cmdline args are :')
for i in sys.argv:
    print(i)
print('\n python路径为',sys.path)
# python函数
# def 函数名 （参数列表）：
# 函数代码块以def关键字为开头，后接函数标识符名称和圆括号()
# 参数放到圆括号中间
# 函数内容以“:”开始，并且缩进。
# return结束函数，选择性返回一个值给调用方，不带表达式的return相当于返回一个none
def hello():
    print("Hello world!")

print(hello())

# calculate the are

def area(width,height):
    return width*height

def print_welcome(name):
    print("welcome",name)

print_welcome("Runoob")

w=4;h=5

print("width=",w,"height=",h,"area=",area(w,h))


# 函数调用

def printme(str):
    print(str)
    return

printme("slslslslsl")
printme("aaaaaaaaaa")


# 参数传递

a=[1,3,4]
b="Runoob"
# 上面变量a和b是没有类型的，只是引用的对象类型不一样，一个是list类型对象，一个是指向String类型的对象

# mutable可更改和immutable不可更改
# string、tuple、number是不可以更改对象，但是list和dict是可以更改的对象
# python中一切都是对象，

# python中传不可变对象实例
def ChangeInt(a):
    a=10
b=2
ChangeInt(b)
print(a)

# 传可变对象实例

def changename(mylist):
    mylist.append([1,3,2,4])
    print("函数内取值：",mylist)
    return

mylist=[10,20,30]
changename(mylist)
print("函数外取值：",mylist)






# 必需参数：必需参数必须以正确顺序传入参数，调用时的数量必须和声明时一样;函数的参数使用不需要指定顺序

def printme(str):
    print(str)
    return
printme("this is Wayne！")
printme(str="This is String")

def printinfo(name,age):
    print("name",name)
    print("age",age)
    return
printinfo(age=50,name='runoob')


# 默认参数，调用函数时，如果没有传递参数，则会使用默认参数。
def printinfo1(name,age=35):
    print("name",name)
    print("age",age)
    return

printinfo1(age=50,name="runoob")
printinfo1(name="Runoob")

# 不定长参数，可能需要一个函数能够处理比当初声明时更多的参数
# 加了*的参数会以元组tuple形式导入，存放所有未命名的变量参数
# 加了**的参数会以字典的形式导入
# 声明函数时，参数中星号*可以单独出现 def f(a,b,*,c) ...
def printinfo2(arg1,*vartuple): #
   print("输出：")
   print(arg1)
   print(vartuple)

printinfo2(70,60,50) # 第一个arg1参数传70，第二个*vartuple传（60,50）


def printinfo3(arg1,*vartuple):
    print("shuchu")
    print(arg1)
    for var in vartuple:
        print(var)
    return

printinfo3(10)
printinfo3(70,60,50)

def printinfo4(arg1,**vardict):
    print("输出")
    print(arg1)
    print(vardict)
    print(arg1,vardict)

printinfo4(1,a=2,b=3)


# 匿名函数 python使用lambda来创建匿名函数
# 匿名函数不再使用def关键字，而是lambda，lambda只是一个表达式，函数体比def简单
# lambda函数有自己的命名空间，而且不能访问自己参数列表之外或者全局命名空间的参数
# lambda表达式： lambda[参数1,参数2: 函数实现]
sum=lambda arg1,arg2:arg1+arg2 #
print(sum(10,20))

# return 语句
# return语句用于退出函数，然后选择性地返回一个表达式，不带参数的return返回none

def sum (arg1,arg2):
    total = arg1+arg2
    print("in function:",total)
    return total

total = sum(10,20)
print("out function:",total)


# 变量作用域 ：python中并不是哪个位置都可以访问的，访问权限决定变量是哪里赋值的。变量的作用域决定了在那一部分程序可以访问
# 特定的变量名称，python的作用域一共有四种：
# L(local)局部作用域,E(Enclosing) 闭包函数外的函数中，G(global)全局作用域，B(Built_in) 内置作用域
# 查找规则为：L->E->G->B ：如果局部找不到，就去局部外的局部进行查找，如果还找不到就去全局找，最后就是去内置函数中找
# 内置作用域是通过一个builtin的标准模块实现，但是这个变量名并不在内置作用域中，所以必须导入这个文件才能使用它。
# python中只要模块（module）、类（class）、函数（def\lambda）才会引入新的作用域，其他的代码块（if-elif-else\try-except）并不会引用新的作用域


g_count=0;# 全局作用域
def outer():
    o_counter=1 #E 闭包函数外的函数中
    def inner():
        i_counter=2 # 局部作用域

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域

total = 0
def sum(arg1,arg2):
    total = arg1+arg2
    print("in funtion:",total)
    return  total

sum(10,20)
print("out function",total)

# golbal 当内部作用域想修改外部作用域的变量时，可以使用global修饰
number=1
def fun1():

    global  number # global定义必须放在函数体最前面
    print(number)

    number=123
    print(number)

fun1()
print(number)

def outer():
    num=10
    def inner():
        nonlocal num
        num=100
        print(num)
    inner()
    print(num)

outer()



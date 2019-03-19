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






# 必需参数：必需参数必须以正确顺序传入参数，调用时的数量必须和声明时一样


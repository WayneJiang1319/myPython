class MyClass:
    i=1234;
    def f(self):
        return "Hello world"

x=MyClass()
print("MyClass 类的属性i为：",x.i)
print("MyClass 类的方法f输出为：",x.f())

# 类的构造方法：__init__()方法，该方法在类的实例时会自动调用，该方法也可以有参数

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart

x=Complex(3.0,-4.5)
print(x.r,x.i)


# self 代表类的实例，而非类
# 类的方法与普通的函数只有一个特殊的区别---它们必须有一个额外的第一个参数名称，按照惯例应该为self

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t=Test()
t.prt()

# 类的方法 def关键字定义一个方法，与一般函数定义不同，类方法必须包含参数self，且为第一个参数，self代表的是类的实例

class people:
    name='' # 定义基本上属性
    age=0   # 定义基本属性
    __weight=0 # 定义私有属性，私有属性在类外无法直接访问
    def __init__(self,n,a,w):# 构造函数
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s 说：我 %d岁。" %(self.name,self.age))


p=people('runoob',10,30)
p.speak()

# 类的继承 clas DerivedCalssName(BaseClassName1)

class people:
    name='' # 定义基本上属性
    age=0   # 定义基本属性
    __weight=0 # 定义私有属性，私有属性在类外无法直接访问
    def __init__(self,n,a,w):# 构造函数
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s 说：我 %d岁。" %(self.name,self.age))

# 单继承
class student (people):
    grade=''
    def __init__(self,n,a,w,g):# 调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self): # 覆写父类的方法
        print("%s 说：我%d岁。我在读%d年级" %(self.name,self.age,self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name=n
        self.topic=t

    def speaker(self):
        print("我叫%s，我是一个演说家，我演讲的主题是%s" %(self.name,self.topic))

class sample (speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test = sample("Tim",25,80,4,"Python")
test.speak()# 当方法名相同时，默认地调用排在前面的父类的方法
#
# s=student('Jim',10,60,3)
# s.speak()

# 多继承



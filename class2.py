# 方法重写
class Parent:
    def myMethod(self):
        print("调用父类的方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")

c=Child()
c.myMethod()
super(Child,c).myMethod()# super函数时用于调用父类（超类）的一个方法

# 如果子类中需要父类的构造方法就需要显式调用父类的构造方法，或者不重写父类的构造方法。
# 子类不重写__init__，实例化会自动调用父类定义的__init__方法
# 如果重写__init__时，要继承父类的构造方法，可以使用super关键字
# super(子类，self).__init__(para1,para2,...)
class Father(object):
    def __init__(self,name):
        self.name=name
        print("name:%s" %(self.name))
    def getName(self):
        return 'Father'+self.name

class Son(Father):
    def __init__(self,name):
        super(Son,self).__init__(name)# son调用父类Father的构造方法
        print("hi")
        self.name=name
    def getName(self):
        return 'Son'+self.name

if __name__=='__main__':
    son=Son('runoob')
    print(son.getName())
# 输出如下：
# name:runoob 子类中没有重写__init__方法，实例化会自动调用父类的__init__方法
# Son runoob   子类重写父类的getName方法，调用子类的getName方法


# 类属性和方法
# 类的私有属性/变量 __private_attrs:两个下划线开头，表明该属性是私有的，不能再类的外部直接访问再类的内部使用时直接
# 使用self.pritvate_attrs
class JustCounter:
    __secretCount=0
    publicCount=0
    def count(self):
        self.__secretCount+=1
        self.publicCount+=1
        print(self.__secretCount)
counter = JustCounter()
counter.count()# 输出：1
counter.count()# 输出：2
print(counter.publicCount) # 输出：2
#print(counter.__secretCount)# 报错



# 类的私有方法：__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部使用，不能再外部调用
class Site:
    def __init__(self,name,url):
        self.name=name # public
        self.__url=url # private para
    def who(self):
        print('name :',self.name)
        print('url:',self.__url)
    def __foo(self): # private method
        print("this is private method")
    def foo(self):
        print("This is public method")
        self.__foo()
x=Site("菜鸟教程",'www.runoob.com')
x.who()
# name:菜鸟教程
# url:www.runoob.com
x.foo()
# This is public method
# This is private method
#x.__foo()
# 报错

# 类的专有方法
# __init__:构造函数，在生成对象时调用
# __del__：析构函数，释放对象时使用
# __repr__：打印，转换
# __setitem__:按照索引赋值
# __getitem__：按照索引获值
# __add__：加运算
# __sub__：减运算


# 运算符重载
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "Vector(%d,%d)"%(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1+v2)

# 输出：Vector(7,8)








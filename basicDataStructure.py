# python中变量是不需要声明的，每个变量在使用前都必须赋值，变量赋值以后变量才会被创建
# python中变量就是变量，没有类型
# python中（=）用来给变量赋值，等号左边是一个变量名，右边是存储在变量中的值

counter = 100
miles = 1000.0
name = "jiangwen"
print(counter)
print(miles)
print(name)

# python 中允许同时为多个变量赋值
a=b=c=1
a,b,c=1,2,'niajf'
print('---------------------------------------------------------------------------------')
# python中标准数据类型 Number（数字）、String（字符串）、List（列表）、Tuple（元组）、Set（集合）、Dictionary（字典）
# Number 数字：int，float，bool，complex
a,b,c,d=2,30.2,True,2+3j
print(type(a),type(b),type(c),type(d)) # type()不会认为子类是父类类型
a = 111
print(isinstance(a,complex))# instance()会认为子类是一种父类类型

print('---------------------------------------------------------------------------------')

# 数值运算
print(5+4)
print(4.3-2)
print(2/4) #/返回一个浮点数
print(2//4)#//返回一个整数
print(17%3)
print(2**5)

# python可以同时为多个变量赋值；一个变量可以通过赋值指向不同的类型对象

print('-------------------------------字符串String--------------------------------------------------')
# String:字符串可以用单引号或者双引号括起来，同时可以使用转义\字符
# 字符串是从左到右是以0位开始位，-1为从右往左开始位
# + 是字符串连接符，* 表示复制当前字符串
# python没有单独的字符类型，一个字符就是长度为1的字符串
# python中字符串不能改变

print('----------------------------------List列表----------------------------------------------------')
# 列表是写在方括号[]之间、用逗号分隔开的元素列表
# 和字符串一样，列表同样可以被索引和截取，被截取后返回一个包含所需元素的新列表
# 索引值以0位开始值，-1为从末尾的开始位置
# +是列表连接运算符，*是重复操作
# 列表中元素是可以改变的
# list写在方括号之间，元素用逗号隔开；list可以被索引和切片；list的元素是可以被改变的
# list的截取是可以设置步长的参数的
list=['abcd',786,2.34,'runoob',70.2]
tinylist=[123,'runoob']
print(list)
print(list[0])
print(list[1:3])# 注意！不包含list[3],只是截取到list[1]和list[2]
print(list[2:])
print(list[-1])
print(tinylist*2)
print(list+tinylist)
list[0]='abdcdedff'
print(list)
print(list[0:3:2])

print('------------------Tuple(元组)-------------------------------------------')
# Tuple与list类似，但是是()表示，元素之间是逗号隔开，而且元组中元素不能修改
# 虽然tuple的元素不可改变，但是它可包含的可变的对象，比如list列表。
# 元组包含0和1个元素是比较特殊的规则
tuple=('abdc',3,4.3,2,1,'runoob')
tinytuple=(123,'runoob')
print(tuple)
print(tuple[0])
print(tuple[-1])
print(tuple[1:4])
print(tuple[3:])
print(tinytuple*2)
print(tuple+tinytuple)
#tuple[2]=1
tup1=()
tup2=(1,)

print('----------------------Set集合--------------------------------------------')
# 集合set是由一个或者数个大小整体组成的，构成集合的事物或者对象称作元素或者成员
# set功能是进行成员关系测试或者删除重复元素
# 使用set{}或者{}创建一个set，但是一个空的set必须是set{}
# set可以进行集合运算
student={'Tom','Jim','Mary','Tom','Jack','Rose'}
print(student)
if 'Rose' in student:
    print('Rose is in Student')
else:
    print('Rose is not in Student')
a = set('abcdef')
b = set('defgh')
print(a)
print(a-b) # 集合a和集合b的差集，以a为准
print(a|b) # 集合a和集合b的并集
print(a&b) # 集合a和b的交集
print(a^b) # a和b中不同时存在的元素

print('------------------------Dictionary字典----------------------------------------')
# 字典dictionary是无序的对象集合，字典当中的元素是通过键来存取的
# dictionary是一种映射类型，用{}标识，是一个无序的key，value集合
# 键key必须是不可变的类型，key而且是必须为唯一
# dictonary也有一些内置函数，比如函数clear(),keys(),values()
# 创建空dictionary时必须使用{}
dict={}
dict['one']='1-cainiaojiaochen'
dict[2]='2-cainiaogongju'
tinydict={'name':'runoob','code':1,'site':'www.runoob.com'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

print('------------------Python数据类型转换-------------------------------------------')

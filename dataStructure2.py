# list是可变的，但是string和tuple是不可变的
# 常见方法：
a=[66.25,333,333,1,1234.5]
# list.count()：计算list的元素出现次数
print(a.count(333),a.count(66.25),a.count('x'))
# list.insert(i,x) 在指定位置插入一个元素，第一个参数是准备插入到其前面的那个元素的索引
a.insert(2,-1)
print(a)
# list.append(x) 将一个元素添加到列表的尾部
a.append(333)
print(a)

# list.index(x)，返回第一个值为x元素的索引值
a.index(333)
print(a.index(333))

# list.remove(x),删除列表值为x的第一个元素，注意是第一个元素
a.remove(333)
print(a)

# list.reverse(),倒排list中所有的元素
a.reverse()
print(a)

# list.sort()，对列表中的元素进行排序
a.sort()
print(a)

# list.clear()，清除列表中元素
a.clear()
print(a)


# 将列表当做堆栈使用 append方法和pop方法，后进先出
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack)
 # list.pop([i]) 从列表的指定位置移除元素，并将其返回；如果没有指定索引，a.pop()将返回最后一个元素，元素随即从列表中删除。
print(stack.pop())
print(stack.pop())
print(stack.pop(2))
print(stack)

# 将list当做队列使用，先进先出 poplef()最左边的元素先离开
from collections import  deque
quene= deque(["Eric","John","Michael"])
quene.append("Terry")
quene.append("Graham")
quene.popleft()
print(quene)
quene.popleft()
print(quene)

# 列表推导式
vec=[2,4,6]
print([3*x for x in vec])

print([[x,x**2] for x in vec])

freshfruit = ['banana','loganberry','passion fruit']
print([weapon.strip() for weapon in freshfruit])

# if
print([3*x for x in vec if x>3])

# 循环
vec1=[2,4,6]
vec2=[4,3,-9]
print([x*y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])

# 嵌套列表分析
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(matrix)

print([[row[i] for row in matrix] for i in range(4)])


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# del 语句

a=[-1,1,66,25,333,333,1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)


# tuple () 元组在输出时总是有括号的，以便表达正确的嵌套结构，在输入时可能没有括号，但是一般是必须要有括号的。
t=(122,222,"ajajh")
print(t[0])
print(t)

# 集合 set
# 集合是一个无序不重复元素的集，基本功能关系包含关系测试和消除重复元素

basket = {'apple','apple','orange'}
print(basket)

print('orange' in basket)

print('tea' in basket)

# 字典 键值对

tel = {'a':123,'b':333}
print(tel)

tel['c']=1254
print(tel)

print(tel['a'])

print(tel.keys())

print(sorted(tel.keys()))

# 构造dict
print(dict([('sape',4139),('guido',4127),('jack',4098)]))

# 遍历字典
# 可以使用items()同时解读出来
dict1={'a':123,'b':23,'c':333,}
for k,v in dict1.items():
    print(k,v)
# 遍历 序列 list 索引和对于值可以使用enumerate()
for i ,v in enumerate(['aa','bb','cc']):
    print(i,v)

# 同时遍历两个或者多个序列，可以使用zip组合
questions = ['name','hobay','color']
answers = ['jiangwen','programming','black']
for q,a in zip(questions,answers):
    print("what is your {0}? it is {1}".format(q,a))
# 反向遍历一个序列，首先指定序列，然后reversed()函数
for i in reversed(range(1,10,2)):
    print(i)
# 字母顺序或者个数顺序来遍历一个序列，使用sorted()函数
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


list1=[1,2,'abdc',30.1]
print(list1[2])
list1[2]='ABDC'
print(list1)
del list1[0]
print(list1)
print(len(list1))
print(3 in list1)
a=['a','b','c']
b=[1,2,3]
x=[a,b]
print(x[0])
print(x[1])
print(max(b))

d=[1,2,4,'a']
d.append('b')
print(d)
print(d.count(1))
d.remove('b')
print(d)
e=list.copy(d)
print(e)
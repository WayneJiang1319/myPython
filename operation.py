print('------------------------算术运算符--------------------------')
a=10
b=21
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(b%a)#返回除法的余数
print(a**b)
print(b//a)

print('------------------------比较运算符---------------------------')
a=21;b=10;c=0
if(a==b):
    print('1-a等于b')
else:
    print('1-a不等于b')

if(a!=b):
    print('yes')
else:
    print('NO')
if(a<b):
    print('yes')
else:
    print('no')
print('-------------------------赋值运算符-----------------------')

a=21;b=10
c=1
c+=b
print(c)
c-=b
print(c)
c*=b
print(c)
c/=b
print(c)
c%=b
print(c)
c**=a
print(c)
c//=a
print(c)
print('----------------------python运算符------------------------')
a=60
b=13
c=0
c=a&b
print(c)
print('-----------------------逻辑运算符--------------------------')
a=20
b=10
c=0

print('a or b =', a or b)
print('-----------------------成员运算符-------------------------')
a=10
b=20
list=[1,2,3,10,30]
if a in list:
    print(True)
else:
    print(False)

if b not in list:
    print(True)
else:
    print(False)

print('-----------------------身份运算符-------------------------')
# is
# is not
n = 100
sum=0
counter=1
while counter<=n:
    sum = sum+counter
    counter+=1
print('from 1 to %d 之和:%d' %(n,sum))

# 无限循环
#

print('--------------------------for循环----------------------------------------')

list = ['c','b','a','d']
for x in  list:
    print(x)

sites=['Baidu','Google','Runoob','Taobao']
for site in sites:
    if site == 'Runoob':
        print('菜鸟教程')
# break执行后，跳出当前for循环或者while循环，同时对应循环的else块将不会再执行
        break
    print('循环数据'+site)
else:
    print("没有循环数据")
print("完成循环！")

# range()函数
for i in range(5):
    print(i)

for a in range(0,10,3) :
    print(a)

b=['Google','Baidu','Runoob','Taobao','QQ']
for i in range(len(b)):
    print(i,b[i])

# continue语句被用来告诉python跳过当前循环中的剩余需要执行的语句，但是继续下一轮循环

for letter in 'Runoob':
    if letter =='o':
        continue
    print('the letter is :',letter)
var = 10
while var > 0:
    var=var-1
    if var==5:
        break
    print('当前变量：',var)
print('byebye')

# the letter is : R
# the letter is : u
# the letter is : n
# the letter is : b
# 当前变量：9
# 当前变量：8
# 当前变量：7
# 当前变量：6
# byebye

print('---------------------------Pass语句------------------------------------')

# pass是空语句，为了保持程序结构的完整性，一般不做任何事，用作占位语句
for letter in 'Runoob':
    if letter =='o':
        pass
        print('run pass ')
    print('the letter is：',letter)
print('Good bye')

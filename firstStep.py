# fibonaci 第三个数等于前两个数之和
# 关键字end可以将结果输出到同一行
a=0;b=1
while b<10:
    print(b,end=',')
    a,b=b,a+b

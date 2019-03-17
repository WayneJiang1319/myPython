# if - elif-else

age=int(input('please input the age of dog:'))
print('')
if age<0:
    print('r u kidding me?')
elif age==1:
    print('the same as child')
elif age==2:
    print('the same as 22')
elif age>2:
    humam=22+(age-2)*5
    print('the same as ',humam)

num=int(input('please input the age '))
if num%2==0:
    if num%3==0:
        print('the num may be 2 and 3')
    else:
        print('it is ....')
else:
    if num%3==0:
        print('the num is aaaa')
    else:
        print('.....................')
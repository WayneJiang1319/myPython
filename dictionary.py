#d={key1:value1,key2:value2}
dict1={'a':'A','b':'B'}
dict2={1:'a',2:'ab',3:2}
dict3={1:'C','A':2}

print(dict1)
print(dict2)
print(dict3)
print(dict1['a'])
print(dict2[2])

dict2[1]='abcde'
print(dict2)

del dict1['a']
print(dict1)
dict1.clear()
print(dict1)

print(len(dict2))
print(str(dict2))
print(type(dict1))

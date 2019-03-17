# list []
# tuple()
# dictionary {}
# set{}

set1={1,1,2,2,4,5}
print(set1)

# add
set1.add(6)
print(set1)
set1.remove(6)
print(set1)
set1.update(['a','b','c'])
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
if 4 in set1:
    print("True")
else:
    print('False')

print(len(set1))
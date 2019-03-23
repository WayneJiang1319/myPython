import os
print(os.name)

path=os.path.abspath(__file__)# 获取文件绝对路径
path2=os.path.dirname(__file__)# 返回文件路径
path3=os.path.dirname(os.path.abspath(__file__))
path4=os.path.split(path3)[0]
path5=os.path.join(path4,"test\ogf","inog")# 连接目录与文件名或者目录

if os.path.exists(path2):# 判断给出路径是否存在
    print("True")
print(path)
print(path2)
print(path3)
print(path4)
print(path5)

if os.path.isfile(path3):# 判断给出的路径是一个文件
    print("It is file")
elif os.path.isdir(path3):# 判断给出的路径是否是一个目标
    print("It is DIR")
else:
    print("we do not know")

print(os.path.getsize(path))# 获取文件的大小
print(os.path.getsize(path4))# 为目录则返回0


print(os.name)
print(os.listdir(path2))


# 模块：模块是一个包含所有定义的函数和变量的文件，后缀名是.py。模块可以被其他程序引入

import sys

print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\n\nPython路径为：',sys.path,'\n')

# import 模块 导入这个模块下所有的函数
# from ... import 从模块中导入指定的函数到命名空间中
# from ... import*


# __name__属性
# 每个模块都有一个__name__属性，当其值是'_main_时'，表明模块自身是在运行的，否则是别引用。

# dir()函数
import sys

print(dir(sys))

# 标准模块

# 包：一种管理python模块命令空间的形式，采用点模块名称
# 在导入一个包的时候，Python会根据sys.path中的目录来寻找这个包中包含的子目录。
# 目录中只有包含一个__init__.py的文件才能被认为是一个包，主要是是避免一个滥俗的名字不小心影响搜索路径中有效模块

# 导入子模块
import sound.effects.echo

from sound.effects  import echo

# 从一个包中导入*
from packageA import *
# 精准的包索引，导入语句遵循如下规则：如果包定义文件__init__.py存在一个__all__的列表变量，那么在使用from package import *
# 将这个列表中的所有名字作为包内容引入
# 推荐 from packageA import xxx.py 引入特定的模块一般不会出错，给一个精准的描述






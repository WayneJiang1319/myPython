# re.match(pattern,string,flags=0)
# 如果匹配成功，re.match()方法返回一个匹配的对象，否则返回none
# pattern :匹配的正则表达式
# string:要匹配的字符串
# flags：标志位

# group(num)或者group()匹配对象函数来获得匹配表达式

import  re
print(re.match('www','www.runoob.com').span())
print(re.match('com','www.runoob.com'))

line="Cats are smarter than dogs"

matchObj=re.match(r)
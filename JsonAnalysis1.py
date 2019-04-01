# python analysis解析
# json是一种轻量级数据交换格式，JavaScript Object Notation
# python3中可以使用json模块对json数据进行解编码
# json.dumps() 对json数据进行编码
# json.load()对数据进行解码
# # python数据结构与Json类型转换关系/<->表示互转，->表示单项装让
# dict  <->object
# list  <->array
# tuple -> array
# str   <->string
# int   <->number(int)
# float <->number(real)
# True  <->true
# False <->false
# None  <->null


import  json

data={'no':1,'name':'Runoob','url':'http://www.runoob.com'}


json_str=json.dumps(data),# 将pyton的dict数据转换为json数据，注意是dumps，而不是dump
print("python-data：",data)
print("Json-data:",json_str)


data1=json.loads(json_str)# 将json数据转换为python的dict类型
print("data1['name']:",data1['name'])
print("data1['url']:",data1['url'])






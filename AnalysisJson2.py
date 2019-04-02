import json

test_dict = {'bigberg':[7600,{1:[['iphone',6300],['Bike',800],['shirt',300]]}]}

print(test_dict)
print(type(test_dict))

# dumps()将数据转换为字符串  编码
json_str = json.dumps(test_dict)
print(json_str)

print(type(json_str))

# loads 将字符串转换为字典 解码
new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))

# dump:将数据写入json文件
with open("record.json","w") as f:
    json.dump(new_dict,f)
    print("加载文件完成...")


# load：把文件打开，并把字符串转换为数据类型
with open("record.json",'r') as load_f:
    load_dct=json.load(load_f)
    print(load_dct)

load_dct['smallberg']=[8200,{1:[['python',81],['shirt',300]]}]
print(load_dct)

with open("record.json","w") as dump_f:

    json.dump(load_dct,dump_f)

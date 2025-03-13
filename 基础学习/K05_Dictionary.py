
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(tinydict) # 输出完整的字典
print(tinydict.keys()) # 输出所有键  
print(tinydict.values()) # 输出所有值

print ("tinydict['name']: ", tinydict['name'])
print ("tinydict['url']: ", tinydict['url'])

# 修改字典
tinydict['name'] = 8     # 更新 name 键对应的值
print(tinydict)

# 添加字典元素
tinydict['Age'] = 20
print(tinydict)

# 删除字典元素
del tinydict['url']
print(tinydict)

# 清空字典
tinydict.clear()     # 清空字典
print(tinydict)

# 删除字典 会报异常，因为字典已经不存在了
# del tinydict         # 删除字典      
# print(tinydict)


# dict.get(key, default=None)
# 返回指定键的值，如果键不在字典中返回 default 设置的默认值
print(tinydict.get('name', '默认值')) # 获取指定键的值，如果值不存在，则返回 ‘默认值’


# 字典推导式
# dict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值

seq = ('name', 'age', 'sex')

tinydict1 = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(tinydict1))
tinydict1 = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(tinydict1))


# 字典的items()方法返回一个列表，其中包含字典中每个键值对的元组
d={1:"a",2:"b",3:"c"}
print(d.items())
result=[]
for k,v in d.items():
    result.append(k)
    result.append(v)
print(result)
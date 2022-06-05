dict1 = {'name': 'tom', 'age': '20', 'gender': '男'}
# 3.1get 函数
print(dict1['name'])   # 如果当前的key值存在，则返回对应值，否则报错
print(dict1.get('name'))
print(dict1.get('id', 110))  # key不存在，返回参数2；如果没有参数2，则返回None
print(dict1.get('ids'))  # key不存在，返回None
# 3.2 keys（） 查找字典中所有的key，返回可迭代的对象
print(dict1.keys())

# 3.3 values()  查找字典中所有的value，返回可迭代的对象
print(dict1.values())

# 3.4 items()  查找字典中所有的键值对，返回可迭代的对象，
# 里面的数据是元组，元组数据1是key，元组数据2是字典key对应的值
print(dict1.items())
dict1 = {'name': 'tom', 'age': '20', 'gender': '男'}
# 4.1 遍历字典中的key
for key in dict1.keys():
    print(key)
# 4.2 遍历字典中的value 值
for value in dict1.values():
    print(value)
# 4.3 遍历字典中的键值对
for item in dict1.items():
    print(item)

# 4.4
for key, value in dict1.items():
    print(f'{key}={value}')
# 字典为可变类型
dict1 = {'name': 'tom', 'age': '20', 'gender': '男'}
# 字典序列[key] = 值
# id 的值是110   增加id
dict1['id'] = 110
print(dict1)
# 修改字典内的值
dict1['name'] = 'ros'
print(dict1)
# 删除字典或指定的键值对  del(dict)
del dict1['name']
print(dict1)
dict1.clear()  # 清空字典内容，但是保留字典格式
print(dict1)
# 如果当前查找的key值存在，则返回对应的值；否则报错

s1 = {10, 20}
# add()增加单一数据 ，集合是可变
s1.add(100)
print(s1)
s1.add(10)  # 集合有去重功能
print(s1)
###  s1.add([10, 20, 30, 40]) #报错，add（）只能增加单个数据，不能增加序列
print(s1)
##### update() 增加数据系列, 不能增加单个数据
s1.update([10, 50, 60, 70])
print(s1)
# remove(): 删除指定数据，如果数据不存在则报错
s1.remove(10)
print(s1)
### s1.remove(30) 数据不存在，报错
s1.discard(30)  # 删除指定数据，数据不存在也不报错
print(s1)
# pop(): 随机删除某个数据，并返回这个数据
del_num = s1.pop()
print(del_num)

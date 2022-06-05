# 1 准备数据
#  八位老师，（列表） 嵌套


# 2. 将八位老师随机分配到三间办公室
#
import random

teachers = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i']
offices = [[], [], []]
# 2. 分配老师到办公室
for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)
i = 1
    # xx[0]  不能是指定的，要求是随机出现
    #列表追加数据  append(选中)  extend insert
#print(num)
for office in offices:
    print(f'办公室{i}的人数是{len(office)}, 老师分别是:' )
#打印老师的人数，打印老师的姓名
    for name in office:
        print(name)
    i += 1

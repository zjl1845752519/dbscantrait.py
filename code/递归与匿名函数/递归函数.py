def sum_numbers(num):
    if num == 1:
        return 1    #出口，求解1以内的数字累加和
    #如果不是1还会继续执行
    return num + sum_numbers(num-1)
sum_result = sum_numbers(3)
print(sum_result)
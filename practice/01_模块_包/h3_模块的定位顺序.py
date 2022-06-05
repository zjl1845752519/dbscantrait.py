def sleep():
    print('我是自定义的sleep')

from time import sleep  #同名模块，调用时，使用的是最后一个模块
sleep(2)
import time
print(time)

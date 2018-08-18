import numpy as np
length = 50
array = sorted(np.random.randint(100, size=length))
print(array)

maxInterval = 0
maxIndex = -1
for i in range(length-1):
    interval = array[i + 1] - array[i]
    if interval > maxInterval:
        maxInterval = interval
        maxIndex = i + 1
interval = array[maxIndex] - array[0]
for t in range(interval, array[-1] - array[0] + 1):
    flag = True
    for i in range(length):
        if array[i] + t <= array[-1] and array[i] + t not in array:
            flag = False
            break
        if array[i] - t >= array[0] and array[i] - t not in array:
            flag = False
            break
    if flag:
        print(t)
        break

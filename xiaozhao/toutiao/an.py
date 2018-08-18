N = int(input().strip())
for n in range(N):
    line = list(map(int, input().strip().split()))
    length = line[0]
    array = line[1:]

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
        if flag:
            print(t)
    #print(array[maxIndex] - array[0])



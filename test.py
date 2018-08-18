def FindNumsAppearOnce(array):
    # write code here
    if not array:
        return
    num = array[0]
    for i in range(1, len(array)):
        num ^= array[i]
    diffIndex = 0
    print(num)
    while num & 0x01 == 0:
        diffIndex += 1
        num = num >> 1
    print(diffIndex)
    num1, num2 = None, None
    for i in range(len(array)):
        if array[i] & (1 << diffIndex):
            print('a', array[i])
            if num1 is None:
                num1 = array[i]
            else:
                num1 ^= array[i]
        else:
            print('b', array[i])
            if num2 is None:
                num2 = array[i]
            else:
                num2 ^= array[i]
    return num1, num2

array = [2,4,3,6,3,2,5,5]
res = FindNumsAppearOnce(array)
print(res)

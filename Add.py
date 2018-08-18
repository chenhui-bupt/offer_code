def Add(num1, num2):
    # write code here
    for i in range(num2):
        flag = 1
        while num1 & flag == flag:
            num1 ^= flag
            flag = flag << 1
        num1 ^= flag
    return num1


print(Add(1, 2))

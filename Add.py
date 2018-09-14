def Add(num1, num2):
    # write code here
    for i in range(num2):
        while num2:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp
    return num1


print(Add(1, 2))

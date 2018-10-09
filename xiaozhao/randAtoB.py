import random

def randAtoB(a, b):
    if a >= b:
        x = random.randint(1, a)
        while x > b:
            x = random.randint(1, a)
        return x
    else:
        A = a
        rand = [lambda a: random.randint(1, a)]
        while A < b:
            rand.append(lambda a: a * (rand[-1](a) - 1) + random.randint(1, a))
            A *= a
            print(A)
        randA = rand[-1]
        x = randA(a)
        while x > b * (A/b):
            x = randA(a)
        return x % b + 1  # [1, b]



for i in range(5):
    print(randAtoB(7, 5))
print('---------------')
for i in range(5):
    print(randAtoB(5, 7))





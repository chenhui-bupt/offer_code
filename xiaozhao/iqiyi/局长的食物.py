N, M, P = list(map(int, input().split()))
foods = list(map(int, input().split()))
for i in range(M):
    action, food = input().split()
    if action == 'A':
        foods[int(food) - 1] += 1
    if action == 'B':
        foods[int(food) - 1] -= 1
print(foods)
sorted_foods = sorted(foods, reverse=True)
index = sorted_foods.index(foods[P-1])
print(index + 1)

"""
3 4 2
5 3 1
B 1
A 2
A 2
A 3"""

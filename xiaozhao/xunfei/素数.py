import math
q = int(input())
for i in range(q):
	k = int(input())
	n = k**2 + 1
	count = 0
	for num in range(2, n + 1):
		flag = True
		for j in range(2, int(math.sqrt(num))+1):
			if num % j == 0:
				flag = False
		if flag:
			count += 1
		if count == k:
			print(num)
			break
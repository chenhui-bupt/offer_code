inputs = list(map(int, input().strip().split()))
n = inputs[0]
nums = inputs[1:]
nums.sort()
if n % 2:
	index = len(nums) //2 +1
	if sum(nums[:index]) > sum(nums[index:]):
		print(sum(nums[index:]), sum(nums[:index]))
	else:
		print(sum(nums[:index]), sum(nums[index:]))
else:
	nums1 = []
	nums2 = []
	for i in range(len(nums)/2):
		if i % 2 == 0:
			nums1.append(nums[i])
			if i+ 1<len(nums) - 1 - i:
				nums1.append(len(nums) - 1 - i)
		else:
			nums2.append(nums[i])
			if i < len(nums) - 1 - i:
				nums2.append(len(nums) - 1 - i)
	if sum(nums1) > sum(nums2):
		print((sum(nums2), sum(nums1)))
	else:
		print((sum(nums1), sum(nums2)))
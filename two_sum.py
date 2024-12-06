nums = [2,4,6,8,10]
target = 12
for i in range(len(nums)):
	for j in nums[i+1:]:
		if nums[i] + j == target:
			for k in range(len(nums)):
				if j == nums[k]:
					print(i,k)
from itertools import combinations

n, s = map(int, input().split())

nums = list(map(int, input().split()))

count = 0

for i in range(1, n+1):
	for num in combinations(nums, i):
		if s == sum(num):
			count += 1

print(count)
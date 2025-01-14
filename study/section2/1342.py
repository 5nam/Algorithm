from itertools import permutations

inputStr = list(input())
n = len(inputStr)
result = set()

for target in permutations(inputStr, n):
	ok = True
	for i in range(n):
		if i == n-1:
			continue
		if target[i] == target[i+1]:
			ok = False
			break
	
	if ok:
		result.add(tuple(target))

print(len(result))
n, m = map(int, input().split())
arr = list(map(int, input().split()))

neg = []
pos = []

for num in arr:
	if num < 0:
		neg.append(-num)
	elif num > 0:
		pos.append(num)

neg = sorted(neg)[::-1]
pos = sorted(pos)[::-1]

result = [] # 방문하는 곳

for p in pos[::m]:
	result.append(p)

for n in neg[::m]:
	result.append(n)

print(2*sum(result) - max(result))
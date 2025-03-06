from itertools import combinations

t = int(input())
case = list()

for _ in range(t):
	n, m = map(int, input().split())
	case.append([n, m])

for i in range(t):
	n, m = case[i][0], case[i][1]
	print(len(list(combinations(range(m), n))))
	# print(len(combinations(n, m)))
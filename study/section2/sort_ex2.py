n = int(input())
lst = []

for _ in range(n):
	lst.append(input())

print('\n'.join(sorted(lst)))
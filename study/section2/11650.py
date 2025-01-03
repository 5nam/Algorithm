n = int(input())

num_list = []

for i in range(n):
	num_list.append(list(map(int, input().split())))

num_list = sorted(num_list, key=lambda x: (x[0], x[1]))

for num in num_list:
	print(' '.join(map(str, num)))

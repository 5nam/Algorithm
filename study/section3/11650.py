n = int(input())

num_list = [list(map(int, input().split())) for _ in range(n)]

num_list = sorted(num_list)

for num in num_list:
	print(num[0], num[1])

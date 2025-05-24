N = int(input())
arr = [0] + list(map(int, input().split(" ")))

max_value = arr[N]
result = 0

for i in range(N, 0, -1):
	if max_value > arr[i]:
		result += (max_value - arr[i])

	else:
		max_value = arr[i]

print(result)
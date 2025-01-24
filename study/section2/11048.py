def func(i, j, s):
	global arr, x, y, m

	# base
	if i == x-1 and j == y-1:
		return arr[i][j] + s

	# recursive
	if i < x-1 and j < y-1:
		value = func(i+1, j, s+arr[i][j])
		if value is not None and value > m:
			m = value

	if i < x-1 and j < y-1:
		value = func(i, j+1, s+arr[i][j])
		if value is not None and value > m:
			m = value

	if i < x-1 and j < y-1:
		value = func(i, j+1, s+arr[i][j])
		if value is not None and value > m:
			m = value

y, x = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(y)]

m = 0

print(func(0,0,0))
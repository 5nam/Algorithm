def search(r, c):
	global ans, R, C, check, dir

	if r < 0 or r >= R or c < 0 or c >= C:
		return
	
	if check[ord(arr[r][c]) - 65]:
		check[ord(arr[r][c]) - 65] = False
		ans -= 1
		return
	
	for d in range(4):
		i, j = dir[d]

		check[ord(arr[r][c]) - 65] = True
		ans += 1
		search(r+i, c+j)
	
	check[ord(arr[r][c]) - 65] = False
	ans -= 1
	return

# n, m 입력받기
R, C = map(int, input().split(" "))

# arr 입력받기
arr = [input() for _ in range(R)]

dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

check = [False] * 26

ans = 1

for n in range(R):
	for m in range(C):
		search(n, m)

print(ans)
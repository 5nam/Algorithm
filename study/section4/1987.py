def search(y, x):
	global R, C, arr, dy, dx, ans, check, count

	# base_case
	if y < 0 or x < 0 or y >= R or x >= C:
		return
	if check[ord(arr[y][x]) - ord('A')]:
		return

	check[ord(arr[y][x]) - ord('A')] = True
	count += 1

	ans = max(ans, count)

	# recursive_base
	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		search(ny, nx)

	check[ord(arr[y][x]) - ord('A')] = False
	count -= 1


# 입력받기
R, C = map(int, input().split())

arr = [input() for _ in range(R)]

# 좌표 이동 설정(상하좌우)
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

ans = 0
count = 0

check = [False] * 26

search(0,0)

print(ans)



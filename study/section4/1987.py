def search(y, x):
	global R, C, arr, dy, dx, ans, st

	# base_case
	if y < 0 or x < 0 or y >= R or x >= C:
		return
	if arr[y][x] in st:
		return

	st.add(arr[y][x])

	ans = max(ans, len(st))

	# recursive_base
	for i in range(4):
		ny = y + i
		nx = x + i

		search(ny, nx)

	st.remove(arr[y][x])


# 입력받기
R, C = map(int, input().split())

arr = [input() for _ in range(R)]

# 좌표 이동 설정(상하좌우)
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

ans = 0

st = set()

search(0,0)

print(ans)



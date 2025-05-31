# 가장 긴 공통 부분 찾는 알고리즘
def get_best(y, x):
	global N, arr

	best = 0
	before = '-'
	cnt = 0

	# 행
	for i in range(N):
		for cur in arr[y][i]:
			if before == cur:
				cnt += 1
			else:
				cnt = 1

			best = max(cnt, best)
			before = cur

	before = '-'
	cnt = 0

	# 열
	for i in range(N):
		for cur in arr[i][x]:
			if before == cur:
				cnt += 1
			else:
				cnt = 1

			best = max(cnt, best)
			before = cur

	return best

N = int(input())

arr = [list(input()) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

best = 0

# 교환 알고리즘
for y in range(N):
	for x in range(N):
		# 모든 행과 열을 한 번씩은 봐야함.
		# 교체 영향력 밖에 있는 행과 열이 최대 일 수 있으므로
		if y == x:
			best = max(get_best(y, x), best)
		for i in range(4):
			ny, nx = y+dy[i], x+dx[i]
			if (0 <= ny < N) and (0 <= nx < N):
				if arr[y][x] != arr[ny][nx]:
					arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]
					best = max(get_best(y, x), best)
					arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]


print(best)


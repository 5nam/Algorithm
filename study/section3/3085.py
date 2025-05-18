# 가장 긴 공통 부분 찾는 알고리즘
def get_best():
	global N, arr

	best = 0
	before = '-'

	for y in range(N):
		cnt = 0
		for x in range(N):
			if before == arr[y][x]:
				cnt +=1
			else:
				cnt = 1

			best = max(cnt, best)
			before = arr[y][x]

	for x in range(N):
		cnt = 0
		for y in range(N):
			if before == arr[y][x]:
				cnt +=1
			else:
				cnt = 1

			best = max(cnt, best)
			before = arr[y][x]

	return best


N = int(input())

arr = [list(input()) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# print(arr)

best = 0

# 교환 알고리즘
for y in range(N):
	for x in range(N):
		temp = 0
		for i in range(4):
			ny, nx = y+dy[i], x+dx[i]

			if (0 <= ny < N) and (0 <= nx < N):
				if arr[y][x] != arr[ny][nx]:
					arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]
					temp = get_best()
					arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]

			best = max(temp, best)

print(best)


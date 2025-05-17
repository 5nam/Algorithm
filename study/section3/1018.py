def get_min(si, sj):
	global arr, sw, sb
	c1 = c2 = 0

	for i in range(8):
		for j in range(8):
			c1 += (arr[si + i][sj + j] != sw[i][j])
			c2 += (arr[si + i][sj + j] != sb[i][j])

	return min(c1, c2)

N, M = map(int, input().split(" "))

# arr = [list(input().split()) for _ in range(N)]

arr = [input() for _ in range(N)]

sw = [['' for _ in range(8)] for _ in range(8)]
sb = [['' for _ in range(8)] for _ in range(8)]


for i in range(8):
	for j in range(8):
		sw[i][j] = ('W' if (i+j) % 2 == 0 else 'B')
		sb[i][j] = ('B' if (i+j) % 2 == 0 else 'W')

best = 100_000

# for i in range((N%8) + (N//8)):
# 	for j in range((M%8) + (M//8)):
# 		if (i+8) >= N or (j+8) >= M:
# 			continue
# 		best = min(best, get_min(i, j))

for i in range(N):
	for j in range(M):
		if (i + 7 >= N) or (j + 7 >= M):
			continue
		best = min(best, get_min(i, j))
	
print(best)
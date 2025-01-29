import sys
sys.setrecursionlimit(int(1e6))

INF = int(1e12)

def func(r, c):

	global dp, arr

	# base case
	if dp[r][c] != -1:
		return dp[r][c]


	# recursive case
	best = INF
	for i in range(3):
		if i != c:
			best = min(best, func(r-1, i))
		
	dp[r][c] = best + arr[r][c]
	return dp[r][c]

n = int(input())

arr = [[0] * 3] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3] + [[-1] * 3 for _ in range(n)]

print(min(func(n, 0), func(n, 1), func(n, 2)))
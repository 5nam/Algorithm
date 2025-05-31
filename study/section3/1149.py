n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr = [[0]*3] + arr

# 초기값 초기화
dp = [[0] * 3 for _ in range(n+1)]

for r in range(1, n+1):
	dp[r][0] = min(dp[r-1][1], dp[r-1][2]) + arr[r][0]
	dp[r][1] = min(dp[r-1][0], dp[r-1][2]) + arr[r][1]
	dp[r][2] = min(dp[r-1][0], dp[r-1][1]) + arr[r][2]


print(min(dp[n][0], dp[n][1], dp[n][2]))
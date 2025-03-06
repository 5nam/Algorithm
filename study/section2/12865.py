N, K = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N)) 

dp = [[[0, 0] for _ in range(N)] for _ in range(N)]

# 초기값 세팅
for i in range(N):
	dp[i][i][0] = arr[i][0]
	dp[i][i][1] = arr[i][1] 

m_v = dp[0][0][1]
# dp 테이블 갱신
for i in range(N):
	for j in range(i+1, N):
		if dp[i][j-1][0] + arr[j][0] <= K:
			dp[i][j][0] = dp[i][j-1][0] + arr[j][0]
			dp[i][j][1] = dp[i][j-1][1] + arr[j][1]

			if m_v < dp[i][j][1]:
				m_v = dp[i][j][1]

		else:
			dp[i][j][0] = dp[i][j-1][0]
			dp[i][j][1] = dp[i][j-1][1]

print(m_v)
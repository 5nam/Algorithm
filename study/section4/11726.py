N = int(input())

# dp 테이블 생성
dp = [0] * (N+2)


dp[1] = 1
dp[2] = 2

# 갱신
for i in range(3, N+1):
	dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[N])
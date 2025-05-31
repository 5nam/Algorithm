N = int(input())

arr = [0] + list(map(int, input().split(" ")))

# dp 테이블 선언 & 초기값 설정
dp = [0] * (N+1)

# dp 테이블 갱신
for i in range(1, N+1):
	dp[i] = max(0, dp[i-1]) + arr[i]

print(max(dp[1:]))

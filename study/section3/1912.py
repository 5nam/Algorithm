N = int(input())

arr = [-100_001] + list(map(int, input().split(" ")))

# print(arr)

# dp 테이블 선언
dp = [-100_001] * (N+1)

# 초기값 세팅
dp[N] = arr[N]

for i in range(N-1, 0, -1):
	# 이전값이 -100,001 이면 dp[i] 에 바로 할당
	if dp[i+1] == -100_001:
		dp[i] = arr[i]
		continue

	# 이전 dp[i+1] + arr[i] 의 합이 이전 값보다 작으면
	if dp[i+1] + arr[i] < dp[i+1]:
		# 현재 i 번째보다 앞의 값과의 합이 이전 dp 값보다 크거나 같으면, 연속으로 하는게 좋으므로 현재값 포함해서 갱신
		if dp[i+1] + arr[i] + arr[i-1] >= dp[i+1]:
			dp[i] = dp[i+1] + arr[i]
		# 작으면, -100_001 값으로 초기화
		else:
			dp[i] = -100_001
		continue

	# dp[i+1] + arr[i] 의 합이 이전 값보다 크거나 같으면 포함으로 갱신
	dp[i] = dp[i+1] + arr[i]

print(max(dp))

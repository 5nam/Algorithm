n = int(input())

arr = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):

	dp[i] = arr[i] + max(0, dp[i-1])

print(max(dp[1:]))
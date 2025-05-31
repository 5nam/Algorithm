N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [-1] * (N+1)

# 초기값 초기화
dp[1] = 1

# DP Table 갱신
for i in range(2, N+1):
    best = 0
    for j in range(1, i):
        if arr[i] > arr[j]:
            best = max(best, dp[j])
    dp[i] = best + 1
    
print(max(dp[1:]))
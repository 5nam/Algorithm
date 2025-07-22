N = int(input())
arr = [0] + list(map(int, input().split()))

ans = 0
dp1 = [0] * (N+1)
dp2 = [0] * (N+1)

# print(arr)

for i in range(1, N+1):
    dp1[i] = 1
    for j in range(1, i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(N, 0, -1):
    dp2[i] = 1
    for j in range(N, i, -1):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(1, N+1):
    ans = max(ans, dp1[i] + dp2[i] - 1)

print(ans)
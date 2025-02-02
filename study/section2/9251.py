arr1 = ['a'] + list(input())
arr2 = ['a'] + list(input())

n = len(arr1)
dp = [0] * n
if arr1[n-1] in arr2:
    dp[n-1] = 1

min_j = 1001
for i in range(len(arr1)-2, 0, -1):
    for j in range(1, len(arr2)):
        if arr1[i] in arr2:
            if arr1[i] == arr2[j]:
                if min_j > j:
                    min_j = j
                    dp[i] = dp[i+1] + 1
                else:
                    dp[i] += 1

print(max(dp))
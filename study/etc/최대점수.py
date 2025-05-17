N, M = map(int, input().split())
T = [0] # 시간
S = [0] # 점수

for _ in range(N):
    s, t = map(int, input().split())
    T.append(t)
    S.append(s)

# DP 테이블 생성 및 초기값 설정
dp = [[0 for _ in range(M+1)] for _ in range(N+1)] # N x M

# DP 갱신
for n in range(1, N+1):
    for m in range(1, M+1):
        dp[n][m] = dp[n-1][m]
        if m - T[n] >= 0:
            dp[n][m] = max(dp[n][m], dp[n-1][m-T[n]]+S[n])

print(dp[n][m])
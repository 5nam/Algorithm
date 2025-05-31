N, K = map(int, input().split())

# 무게와 가치를 담는 배열. 1인덱스로 사용할 것이므로 [0] 으로 선언해줌
W = [0]
V = [0]

for _ in range(N):
	w, v = map(int, input().split())
	W.append(w)
	V.append(v)

# 초기값 0 으로 세팅 및 DP 테이블 생성
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# dp 테이블 갱신
for n in range(1, N+1):
	for k in range(1, K+1):
		dp[n][k] = dp[n-1][k]
		if k - W[n] >= 0:
			dp[n][k] = max(dp[n][k], dp[n-1][k-W[n]] + V[n])

print(dp[N][K])
# 입력받기
R, C = map(int, input().split())

# 둘이 뭐가 다른지 정리하기
# arr = list('a' * C) + list('a' + input() for _ in range(R))
arr = ['a' * C] + list('a' + input() for _ in range(R))

# 좌표 이동 설정
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# dp 테이블
dp = list([0] * (C+2) for _ in range(R+2))

# # dp 초기화
# dp[1][1] = 1

# 중복 값인지 체크하는 set 생성
s_list = set()
# s_list.add(arr[1][1])

# dp 갱신
for r in range(1, R+1):
	for c in range(1, C+1):
		if arr[r][c] not in s_list:
			dp[r][c] = max(
				dp[r+dy[0]][c+dx[0]],
				dp[r+dy[1]][c+dx[1]],
				dp[r+dy[2]][c+dx[2]],
				dp[r+dy[3]][c+dx[3]]
			) + 1
			s_list.add(arr[r][c])

		else:
			break

print(dp)

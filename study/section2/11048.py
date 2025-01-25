import sys
sys.setrecursionlimit(1000000)

def func(i, j):
	global arr, f

	if f[i][j] != -1:
		return f[i][j]
	
	f[i][j] = max(func(i-1, j), func(i, j-1), func(i-1, j-1)) + arr[i][j]
	return f[i][j]

r, c = map(int, input().split())

# n+1 x m+1	행렬 만들기
arr = [[0] + list(map(int, input().split())) for _ in range(r)] # 0행 추가
arr = [[0] * (c + 1)] + arr # 0열 추가

f = [[-1 for _ in range(c+1)] for _ in range(r+1)]

# 초기값 설정 : 0
for j in range(0, c + 1):
    f[0][j] = 0

for i in range(0, r + 1):
    f[i][0] = 0
    
print(func(r, c))
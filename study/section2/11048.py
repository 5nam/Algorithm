r, c = map(int, input().split())

# n+1 x m+1	행렬 만들기
arr = [[0] + list(map(int, input().split())) for _ in range(r)] # 0행 추가
arr = [[0] * (c + 1)] + arr # 0열 추가

f = [[0 for _ in range(c+1)] for _ in range(r+1)]
    
for i in range(1, r+1):
    for j in range(1, c+1):
        f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1]) + arr[i][j]
    
print(f[r][c])
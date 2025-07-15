def solution(r, c):

    global R, C, arr, cur, ans, dir, check

    if r < 0 or r >= R or c < 0 or c >= C:
        return
    if check[ord(arr[r][c]) - ord('A')]:
        return
    
    check[ord(arr[r][c]) - ord('A')] = True
    cur += 1

    ans = max(cur, ans)

    for i, j in dir:
        n_r = r + i
        n_c = c + j
        solution(n_r, n_c)
    
    check[ord(arr[r][c]) - ord('A')] = False
    cur -= 1


# 입력받기
R, C = map(int, input().split())

arr = [input() for _ in range(R)]

# 필요한 변수 선언하기
cur, ans = 0, 0
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
check = [False] * 26

solution(0,0)

print(ans)
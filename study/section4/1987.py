<<<<<<< HEAD
def search(r, c):
	global ans, R, C, check, dir

	if r < 0 or r >= R or c < 0 or c >= C:
		return
	
	if check[ord(arr[r][c]) - 65]:
		check[ord(arr[r][c]) - 65] = False
		ans -= 1
		return
	
	for d in range(4):
		i, j = dir[d]

		check[ord(arr[r][c]) - 65] = True
		ans += 1
		search(r+i, c+j)
	
	check[ord(arr[r][c]) - 65] = False
	ans -= 1
	return

# n, m 입력받기
R, C = map(int, input().split(" "))
=======
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
>>>>>>> b75e57bb1f95122ef31b26151c063fa1925896e5

# arr 입력받기
arr = [input() for _ in range(R)]

<<<<<<< HEAD
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

check = [False] * 26

ans = 1

for n in range(R):
	for m in range(C):
		search(n, m)
=======
# 필요한 변수 선언하기
cur, ans = 0, 0
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
check = [False] * 26

solution(0,0)
>>>>>>> b75e57bb1f95122ef31b26151c063fa1925896e5

print(ans)
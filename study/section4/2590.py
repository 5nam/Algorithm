def is_possible(y, x, n):
	global arr

	for c in range(9):
		if arr[y][c] == n:
			return False

	for r in range(9):
		if arr[r][x] == n:
			return False

	# 사각형 배열 만들기
	y = (y//3)*3
	x = (x//3)*3
	for r in range(y, y+3):
		for c in range(x, x+3):
			if arr[r][c] == n:
				return False

	return True

# def fill_row(y):
# 	global cnt, arr

# 	temp = sorted(arr[y])
# 	fill_num = get_fill_num(temp)

# 	if fill_num:
# 		for x in range(9):
# 			if arr[y][x] == 0:
# 				arr[y][x] = fill_num
# 				return True

# 	return False

# def fill_column(x):
# 	global cnt, arr

# 	temp = []

# 	# 뒤집기
# 	for y in range(9):
# 		temp.append(arr[y][x])

# 	temp = sorted(temp)
# 	fill_num = get_fill_num(temp)

# 	if fill_num:
# 		for y in range(9):
# 			if arr[y][x] == 0:
# 				arr[y][x] = fill_num
# 				return True

# 	return False

# def fill_rectangle(i, j):
# 	global cnt, arr

# 	temp = []

# 	# 사각형 배열 만들기
# 	i = (i//3)*3
# 	j = (j//3)*3
# 	for y in range(i, i+3):
# 		for x in range(j, j+3):
# 			temp.append(arr[y][x])

# 	temp = sorted(temp)
# 	fill_num = get_fill_num(temp)

# 	if fill_num:
# 		for y in range(i, i+3):
# 			for x in range(j, j+3):
# 				if arr[y][x] == 0:
# 					arr[y][x] = fill_num
# 					return True

# 	return False

def fill_up(lev):
	global arr, pos

	# base case
	if lev == len(pos):
		for row in arr:
			print(" ".join(map(str, row)))
		print()
		exit(0)
		return

	y, x = pos[lev]

	# recursive case
	for n in range(1, 10):
		if is_possible(y, x, n):
			arr[y][x] = n
			fill_up(lev+1)
			arr[y][x] = 0

# 입력받기
arr = [list(map(int, input().split())) for _ in range(9)]

# 채워야 하는 좌표 저장
pos = []
for i in range(9):
	for j in range(9):
		if arr[i][j] == 0:
			pos.append((i, j))

# 채우기
fill_up(0)



def get_new_arr2():
	global arr
	result = []
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			temp = []
			for n in range(i, i+3):
				for m in range(j, j+3):
					temp.append(arr[n][m])
		
			result.append(temp)
	
	return result

def fill_row(i):
	global cnt, arr

	fill_num = 0
	temp = sorted(arr[i])
	for n in range(1, 10):
		if temp[n-1] != n:
			fill_num = n

	for j in range(9):
		if arr[i][j] == 0:
			arr[i][j] = fill_num
			cnt -= 1
			return

def fill_column(i):
	global cnt, new_arr, arr

	fill_num = 0
	temp = sorted(new_arr[i])
	for n in range(1, 10):
		if temp[n-1] != n:
			fill_num = n

	for j in range(9):
		if arr[j][i] == 0:
			arr[j][i] = fill_num
			cnt -= 1
			return

def fill_rectangle(i, j):
	global cnt, arr, new_arr2

	fill_num = 0
	temp = sorted(new_arr2)

	for n in range(1,10):
		if temp[n-1] != n:
			fill_num = n

	for n in range(i+3):
		for m in range(j+3):
			if arr[n][m] == 0:
				arr[n][m] = fill_num
				cnt -= 1
				return

def check_cnt(arr):
	c = 0
	for i in range(9):
		if arr[i] == 0:
			c += 1

	return c == 1

# 입력받기
arr = [list(map(int, input().split())) for _ in range(9)]
new_arr = []
new_arr2 = []

# 0 개수 설정
cnt = 0
for i in range(9):
	for j in range(9):
		if arr[i][j] == 0:
			cnt += 1

# 채우기
while(cnt != 0):
	for i in range(9):
		if check_cnt(arr[i]):
			fill_row(i)


	new_arr = list(map(list, zip(*arr)))
	for i in range(9):
		if check_cnt(new_arr[i]):
			fill_column(i)

	# new_arr2 = get_new_arr2()
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			new_arr2 = []
			for n in range(i, i+3):
				for m in range(j, j+3):
					new_arr2.append(arr[n][m])
			
			if check_cnt(new_arr2):
				fill_rectangle(i, j)

	# for i in range(9):
	# 	if check_cnt(new_arr2[i]):
	# 		fill_rectangle(i)

for row in arr:
    print(" ".join(map(str, row)))

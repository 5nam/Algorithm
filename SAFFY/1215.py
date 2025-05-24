def get_paindrome(i):
	global N, arr, result

	# 열
	for y in range(8-N+1):
		stack = []
		flag = True
		check = True
		for x in range(N):
			if N % 2 != 0: # 홀수
				if x == (N//2):
					flag = False
					continue
				if(flag):
					stack.append(arr[i][y+x])
					continue
				else:
					if(stack and stack.pop() != arr[i][y+x]):
						check = False
						break
			else: # 짝수
				if x == (N//2):
					flag = False
				if(flag):
					stack.append(arr[i][y+x])
					continue
				else:
					if(stack and stack.pop() != arr[i][y+x]):
						check = False
						break

		result += check

	# 행
	for y in range(8-N+1):
		stack = []
		flag = True
		check = True
		for x in range(N):
			if N % 2 != 0: # 홀수
				if x == (N//2):
					flag = False
					continue
				if(flag):
					stack.append(arr[y+x][i])
					continue
				else:
					if(stack and stack.pop() != arr[y+x][i]):
						check = False
						break
			else: # 짝수
				if x == (N//2):
					flag = False
				if(flag):
					stack.append(arr[y+x][i])
					continue
				else:
					if(stack and stack.pop() != arr[y+x][i]):
						check = False
						break

		result += check


# 입력받기
N = int(input())
arr = [input() for _ in range(8)]

# 순회
result = 0

for i in range(8):
	get_paindrome(i)

print(result)




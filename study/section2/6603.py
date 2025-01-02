lst = []
choose = []
k = []
R = 6

# 입력받기
while True:
	temp = list(map(int, input().split(" ")))

	if temp[0] == 0:
		break

	k.append(temp[0])
	lst.append(temp[1:])

# 출력하는 함수 구현
def prt(choose):
	for value in choose:
		print(value, end=" ")
	print()

# 조합 구하는 함수 구현(재귀)
def combination(index, level, k, l):
	if level == R:
		prt(choose)
		return

	for i in range(index, k):
		choose.append(l[i])
		combination(i+1, level+1, k, l)
		choose.pop()

for i in range(len(lst)):
	combination(0,0,k[i],lst[i])
	print()


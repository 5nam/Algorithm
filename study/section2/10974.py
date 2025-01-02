n = int(input())

lst = list(i for i in range(1, n+1))
choose = []
check = [False] * n

def prt(data):
	for value in data:
		print(value, end=" ")
	print()

def permutation(level):
	if level == n:
		prt(choose)

	for i in range(0, n):
		if check[i]:
			continue

		choose.append(lst[i])
		check[i] = True

		permutation(level + 1)

		check[i] = False
		choose.pop()

permutation(0)

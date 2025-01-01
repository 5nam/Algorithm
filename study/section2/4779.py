def f(n):
	global arr
	global g

	if n == 0:
		return arr
	for i in range(0, g, n):
		if i % 2 == 0:
			continue
		for j in range(i, i+n):
			arr[j] = False

	return f(n//3)

lines = []
result = []
while True:
    try:
        line = input()
        
        if line == "":  # 빈 줄이 입력되면 종료
            break
        
        lines.append(int(line))

    except EOFError:  # EOF를 만나면 반복 종료
        break

for i in lines:
	n = i
	g = 1

	for i in range(n):
		g = g*3

	arr = [True] * g

	result.append(f(g//3))


for i in range(len(result)):
	for j in range(len(result[i])):
		if result[i][j]:
			print("-", end="")
		else:
			print(" ", end="")

	print()
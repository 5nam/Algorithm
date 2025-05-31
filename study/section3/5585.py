coin = [500, 100, 50, 10, 5, 1]
num = 1000 - int(input())
cnt = 0

for i in range(len(coin)):
	if num == 0:
		break
	cnt += num // coin[i]
	num %= coin[i]

print(cnt)
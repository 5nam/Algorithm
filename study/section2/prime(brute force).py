n = 1000
result = 0

for i in range(1, n+1):

	if i == 1:
		continue

	isPrime = True

	for j in range(2, i):
		if i%j == 0:
			isPrime = False
			break

	if isPrime:
		result = result + 1

print(result)
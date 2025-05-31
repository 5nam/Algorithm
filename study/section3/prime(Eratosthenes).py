from math import sqrt

n = int(1e6)
is_prime = [True] * (n+1)
is_prime[1] = False
result = 0

for i in range(2, int(sqrt(n))+1):
	if not is_prime[i]:
		continue

	for j in range(i*2, n+1, i):
		is_prime[j] = False

for i in range(1, n+1):
	if is_prime:
		result = result + 1

print(result)
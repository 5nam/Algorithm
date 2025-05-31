from math import sqrt

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n))+1):
		if n%i == 0:
			s.add(i)
			s.add(n // i)

	return s

print(get_divisors(18))
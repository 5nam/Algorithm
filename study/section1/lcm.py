from math import sqrt

def get_divisors(n):
	s = set()

	for i in range(1, int(sqrt(n))+1):
		if n%i == 0:
			s.add(i)
			s.add(n//i)

	return s

def get_gcd(a, b):
	divisors_a = get_divisors(a)
	divisors_b = get_divisors(b)

	return max((divisors_a & divisors_b))

def get_lcm(a, b):
	gcd = get_gcd(a,b)

	return (a*b)//gcd

print(get_lcm(12, 8))
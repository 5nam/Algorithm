
# def get_gcd(a, b):

# 	mod = 1
# 	while mod != 0:
# 		result = mod
# 		mod = a % b
# 		a = b
# 		b = mod

# 	return result

def get_gcd(a, b):
	if b == 0:
		return a

	return get_gcd(b, a%b)

print(get_gcd(12, 8))


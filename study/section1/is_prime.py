from math import sqrt

N = 120
is_prime = [True] * (N+1) # 처음에는 모두 true 로 초기화
is_prime[1] = False # 1은 소수가 아니므로

# 에라토스테네스의 체 알고리즘
for i in range(2, int(sqrt(N)) + 1):
	if not is_prime[i]: # 이미 소수가 아니라면 배수를 살펴볼 필요 X
		continue

	for j in range(2*i, N+1, i): # i 를 제외하고 2번째부터 2*i 부터 N+1 까지 i 의 간격으로
		is_prime[j] = False

for i in range(1, N+1):
	print(i, is_prime[i])

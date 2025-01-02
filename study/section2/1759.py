from itertools import combinations

# 입력받기
L, C = map(int, input().split())

arr = sorted(list(input().split()))

# 조합 구하기
lst = list(combinations(arr, L))

# 정답이 담길 리스트
result = []

def isPossible(lst):
	vowel = ['a', 'e', 'i', 'o', 'u']

	# 모음 개수 구하기
	v = 0
	for value in lst:
		if value in vowel:
			v = v+1

	# 자음 개수 구하기
	c = L - v

	return (v > 0 and c > 1)


for value in lst:
	if isPossible(value):
		result.append(value)

for res in result:
	print(''.join(res))



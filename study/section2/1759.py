from itertools import combinations

# 입력받기
L, C = map(int, input().split())

arr = sorted(list(input().split()))

# 조합 구하기
lst = list(combinations(arr, L))

# 정답이 담길 리스트
result = []

def existVowel(lst):
	vowel = ['a', 'e', 'i', 'o', 'u']

	for value in lst:
		if value in vowel:
			return True

	return False



def existTwoConsonant(lst):
	vowel = ['a', 'e', 'i', 'o', 'u']
	cnt = 0

	for value in lst:
		if value not in vowel:
			cnt = cnt+1

	return cnt > 1


for value in lst:
	if existVowel(value) and existTwoConsonant(value):
		result.append(value)

def prt(res):
	for i in res:
		for j in i:
			print(j, end="")
	print()

for res in result:
	prt(res)



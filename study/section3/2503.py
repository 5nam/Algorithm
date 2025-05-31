from itertools import permutations

n = int(input())

inputNum = [input().split() for _ in range(n)]

result = 0

for cur in permutations(range(1, 10), 3):
	for num, st, bl in inputNum:
		ok = True
		count_st = count_bl = 0

		for i in range(3):
			if str(cur[i]) == num[i]:
				count_st += 1
			elif str(cur[i]) in num: # str 타입으로 in 연산자 이용하여 문자열 중에 cur[i] 가 있는지 확인
				count_bl += 1

		if count_st != int(st) or count_bl != int(bl):
			ok = False
			break

	result += ok # True 는 1 이고, False 는 0 이므로 이렇게 해도 되는 것

print(result)
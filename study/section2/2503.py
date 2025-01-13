from itertools import permutations

n = int(input())

inNum = [list(input().split()) for i in range(n)]

allNum = list(map(list, permutations([1,2,3,4,5,6,7,8,9], 3)))

result = set()

for i in range(0, n):
	num = list(map(int, inNum[i][0]))
	

	for j in range(0, len(allNum)):
		temp = list(allNum[j])
		strike = 0
		ball = 0
		
		for k in range(0, 3):
			for l in range(0, 3):
				if num[k] == temp[l]:
					if k == l:
						strike = strike+1
					else:
						ball = ball+1

		if inNum[i][1] != strike or inNum[i][2] != ball:
			print(temp)
			result.add(tuple(temp)) # 지금 풀이가 틀린 이유. temp 의 인덱스와 result 의 인덱스가 일치하지 않으므로 엉뚱한 값을 지우는 것..
			

print(len(allNum) - len(result))
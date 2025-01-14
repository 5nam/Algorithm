
def func(lev):
	global chars, choose, cnt, s, result

	# base case
	if lev == len(s):
		result += 1
		return

	# recursive case
	for c in chars:
		if cnt[c] == 0:
			continue

		if (not choose) or (choose[-1] != c): # 되는 경우만 살펴보는 것
			cnt[c] -= 1
			choose.append(c)
			func(lev+1)
			cnt[c] += 1
			choose.pop()

s = input()
chars = set()
cnt = dict()

for c in s:
	chars.add(c) # s 에 있는 문자들 중복 없이 저장
	if c not in cnt: # cnt 에 c 로 된 것 없으면 생성
		cnt[c] = 0

	cnt[c] += 1 # c 로 된 것 +1 해서 개수 세기

choose = []
result = 0

func(0)

print(result)
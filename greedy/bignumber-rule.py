import time

n, m, k = map(int, input().split(' '))

if k > m:
    exit

#2. 1차원 배열 입력받기 = 정수형 리스트로 저장
numbers = list(map(int, input().split(' ')))

numbers.sort(reverse=True)

count = 0
result = 0

for _ in range(m):

    if count == k:
       result += numbers[1]
       count = 0
       continue

    result += numbers[0]
    count += 1

print(result)

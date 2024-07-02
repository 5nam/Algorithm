n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
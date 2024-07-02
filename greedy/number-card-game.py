n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

for index in range(n):
    min_num = []
    min_num.append(min(data[index]))

print(max(min_num))
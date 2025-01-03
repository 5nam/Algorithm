n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr = sorted(arr, key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

print(arr[0][0], arr[1][0], arr[2][0])
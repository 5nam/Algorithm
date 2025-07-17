def solution(before, lev):
    global n, arr, check, ans, cur
    
    # base_case
    # if lev == n:
    #     return
    
    if lev < 0 or lev >= n:
        return
    
    if check[lev]:
        return
    
    # recusrive_case
    if before > arr[lev]:
        before = arr[lev]
        cur += 1

    ans = max(ans, cur)
    
    check[lev] = True
    
    # 왼쪽 방향
    solution(before, lev - 1)
            
    # 오른쪽 방향
    solution(before, lev + 1)
    
    check[lev] = False

    
n = int(input())
arr = list(map(int, input().split()))

target = min(arr)

before = 1_000

left_dp = [0] * n
right_dp = [0] * n

# 왼쪽 방향
for mid in range(n):
    cur = 1
    before = arr[mid]
    
    if arr[mid] == target:
        if not mid == 0 or next == n-1:
            left_dp[mid] = 1
            continue
        
    for next in range(mid-1, -1, -1):
        if (not target == arr[next]) and (before > arr[next]) and (not arr[mid] == arr[next]):
            cur += 1
            before = arr[next]
        
        elif target == arr[next]:
            if next == 0 or next == n-1:
                cur += 1
                before = arr[next]
            
    left_dp[mid] = cur

before = 1_000

# 오른쪽 방향
for mid in range(n-1, -1, -1):
    cur = 1
    before = arr[mid]
    
    if arr[mid] == target:
        if not mid == 0 or next == n-1:
            right_dp[mid] = 1
            continue
        
    for next in range(mid+1, n):
        if (not target == arr[next]) and (before > arr[next]) and (not arr[mid] == arr[next]):
            cur += 1
            before = arr[next]
        
        elif target == arr[next]:
            if next == 0 or next == n-1:
                cur += 1
                before = arr[next]
            
    right_dp[mid] = cur
    

print(left_dp, right_dp)
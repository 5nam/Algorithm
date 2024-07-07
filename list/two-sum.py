def two_sum(nums, target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if(nums[i] + nums[j] == target):
                return True
            
    return False

nums = [4, 1, 9, 7, 5, 3, 16]
target = 14

print(two_sum(nums, target))
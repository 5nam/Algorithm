nums = list(map(int, input().split()))

print(' '.join(map(str, sorted(nums))))
print(' '.join(map(str, sorted(nums, reverse=True))))
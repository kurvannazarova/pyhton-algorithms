nums = list(map(int, input().split()))

s = sum(nums)
min_val = min(nums)
max_val = max(nums)

min_sum = s - max_val
max_sum = s - min_val

print(min_sum, max_sum)
import sys

input = sys.stdin.readline

t = int(input())

nums = [0, 1, 2, 4] + [0] * 7

for _ in range(t):
    n = int(input())

    for i in range(4, n + 1):
        nums[i] = nums[i-3] + nums[i-2] + nums[i-1]
    
    print(nums[n])